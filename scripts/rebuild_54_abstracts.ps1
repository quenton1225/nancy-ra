$ErrorActionPreference = 'Continue'

$inputPath = 'docs/53_fulltext_priority40_balanced.csv'
$outputPath = 'docs/54_crossref_abstracts_40.csv'

function Clean-Text([string]$s) {
  if (-not $s) { return '' }
  return (($s -replace '<[^>]+>', ' ' -replace '\\s+', ' ').Trim())
}

function Decode-InvertedIndex($idx) {
  if (-not $idx) { return '' }
  $pairs = @()
  foreach ($p in $idx.PSObject.Properties) {
    $word = $p.Name
    foreach ($pos in $p.Value) {
      $pairs += [PSCustomObject]@{ pos = [int]$pos; word = $word }
    }
  }
  if ($pairs.Count -eq 0) { return '' }
  $ordered = $pairs | Sort-Object pos
  return (($ordered | ForEach-Object { $_.word }) -join ' ')
}

function Looks-Truncated([string]$s) {
  if (-not $s) { return $true }
  $t = $s.Trim()
  if ($t.EndsWith('...')) { return $true }
  if ($t.Length -lt 220) { return $true }
  return $false
}

$rows = Import-Csv $inputPath
$out = @()

foreach ($r in $rows) {
  $doi = ($r.source_url -replace '^https?://doi.org/', '').Trim().ToLower()

  $title = ''
  $abstractCrossref = ''
  $abstractOpenAlex = ''
  $abstractS2 = ''
  $keywords = ''
  $source = ''

  try {
    $cr = Invoke-RestMethod -Uri ("https://api.crossref.org/works/" + $doi) -Method Get -TimeoutSec 30
    $m = $cr.message
    if ($m.title) { $title = $m.title[0] }
    $abstractCrossref = Clean-Text $m.abstract
    if ($m.subject) { $keywords = (($m.subject | Select-Object -First 8) -join '; ') }
  } catch {}

  try {
    $oa = Invoke-RestMethod -Uri ("https://api.openalex.org/works/https://doi.org/" + $doi) -Method Get -TimeoutSec 30
    if (-not $title -and $oa.display_name) { $title = $oa.display_name }
    $abstractOpenAlex = Clean-Text (Decode-InvertedIndex $oa.abstract_inverted_index)
    if (-not $keywords -and $oa.concepts) {
      $keywords = (($oa.concepts | Select-Object -First 8 | ForEach-Object { $_.display_name }) -join '; ')
    }
  } catch {}

  try {
    $s2 = Invoke-RestMethod -Uri ("https://api.semanticscholar.org/graph/v1/paper/DOI:" + $doi + "?fields=title,abstract") -Method Get -TimeoutSec 30
    if (-not $title -and $s2.title) { $title = $s2.title }
    $abstractS2 = Clean-Text $s2.abstract
  } catch {}

  $candidates = @()
  if ($abstractCrossref) {
    $score = 3
    if (Looks-Truncated $abstractCrossref) { $score = 1 }
    $candidates += [PSCustomObject]@{src='crossref'; abs=$abstractCrossref; score=$score}
  }
  if ($abstractOpenAlex) {
    $score = 3
    if (Looks-Truncated $abstractOpenAlex) { $score = 1 }
    $candidates += [PSCustomObject]@{src='openalex'; abs=$abstractOpenAlex; score=$score}
  }
  if ($abstractS2) {
    $score = 3
    if (Looks-Truncated $abstractS2) { $score = 1 }
    $candidates += [PSCustomObject]@{src='semantic_scholar'; abs=$abstractS2; score=$score}
  }

  if ($candidates.Count -gt 0) {
    $best = $candidates | Sort-Object score, @{Expression={ $_.abs.Length }} -Descending | Select-Object -First 1
    $source = $best.src
    $abstractFinal = $best.abs
  } else {
    $source = ''
    $abstractFinal = ''
  }

  $out += [PSCustomObject]@{
    record_id = $r.record_id
    doi = $doi
    title = $title
    has_abstract = [bool]$abstractFinal
    abstract_source = $source
    abstract = $abstractFinal
    subject_keywords = $keywords
  }
}

$out | Export-Csv -Path $outputPath -NoTypeInformation -Encoding UTF8

"coverage summary"
$out | Group-Object has_abstract | Select-Object Name, Count | Format-Table -AutoSize
"source summary"
$out | Group-Object abstract_source | Select-Object Name, Count | Format-Table -AutoSize
