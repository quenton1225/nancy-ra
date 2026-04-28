const passages = [
  {
    id: 'p1',
    text: 'Adaptive learning systems adjust content, pacing, or support based on learner signals. In inclusive education, the goal is not to label students, but to notice when a learner may need a clearer explanation, a slower pace, or a different presentation format.'
  },
  {
    id: 'p2',
    text: 'Webcam-based eye tracking estimates where a learner is looking by using a standard camera. The signal is noisier than a research-grade eye tracker, but it can be useful for low-risk measures such as reading time, off-screen gaze, and attention shifts.'
  },
  {
    id: 'p3',
    text: 'A careful educational system should fail softly. If a model is uncertain, it should offer optional support rather than make high-stakes decisions. This principle is especially important when working with students who may have special educational needs.'
  }
];

const quiz = [
  {
    id: 'q1',
    question: 'What is the safer goal for the pilot?',
    options: ['Diagnose students', 'Infer learning-state support needs', 'Replace teachers'],
    answer: 'Infer learning-state support needs'
  },
  {
    id: 'q2',
    question: 'Why should the system fail softly?',
    options: ['Because webcam data can be noisy', 'Because CSV files are large', 'Because reading is always easy'],
    answer: 'Because webcam data can be noisy'
  },
  {
    id: 'q3',
    question: 'What data does this MVP export?',
    options: ['Video recordings', 'Gaze coordinates and task responses', 'Face images'],
    answer: 'Gaze coordinates and task responses'
  }
];

const sessionId = `S${Date.now()}`;
let participantId = 'P001';
let currentPassage = 0;
let currentPhase = 'setup';
let currentTrialId = '';
let started = false;
let rows = [];
let calibrationClicks = 0;

const panels = ['setup', 'calibration', 'reading', 'probe', 'quiz', 'done'];
const statusEl = document.getElementById('status');
const participantInput = document.getElementById('participantId');
const startBtn = document.getElementById('startBtn');
const exportBtn = document.getElementById('exportBtn');
const calibrationArea = document.getElementById('calibrationArea');
const passageText = document.getElementById('passageText');
const passageCounter = document.getElementById('passageCounter');
const continueBtn = document.getElementById('continueBtn');
const probeSubmitBtn = document.getElementById('probeSubmitBtn');
const quizSubmitBtn = document.getElementById('quizSubmitBtn');
const quizItems = document.getElementById('quizItems');

function setStatus(message) {
  statusEl.textContent = message;
}

function showPanel(id) {
  currentPhase = id;
  panels.forEach((panelId) => {
    document.getElementById(panelId).classList.toggle('active', panelId === id);
  });
  logEvent('phase_start', id);
}

function baseRow(eventType, eventValue = '') {
  return {
    participant_id: participantId,
    session_id: sessionId,
    timestamp_ms: Math.round(performance.now()),
    phase: currentPhase,
    trial_id: currentTrialId,
    gaze_x: '',
    gaze_y: '',
    page_width: window.innerWidth,
    page_height: window.innerHeight,
    event_type: eventType,
    event_value: eventValue,
    text_id: passages[currentPassage]?.id || '',
    probe_tut: '',
    difficulty: '',
    familiarity: '',
    comprehension_correct: ''
  };
}

function logEvent(eventType, eventValue = '', extra = {}) {
  rows.push({ ...baseRow(eventType, eventValue), ...extra });
}

function logGaze(data) {
  if (!started || !data) return;
  rows.push({
    ...baseRow('gaze'),
    gaze_x: Number.isFinite(data.x) ? data.x.toFixed(2) : '',
    gaze_y: Number.isFinite(data.y) ? data.y.toFixed(2) : ''
  });
}

function buildCalibrationTargets() {
  calibrationArea.innerHTML = '';
  const positions = [
    [10, 10], [50, 10], [90, 10],
    [10, 50], [50, 50], [90, 50],
    [10, 90], [50, 90], [90, 90]
  ];
  positions.forEach(([left, top], index) => {
    const target = document.createElement('button');
    target.type = 'button';
    target.className = `target ${index === 0 ? 'active-target' : ''}`;
    target.style.left = `${left}%`;
    target.style.top = `${top}%`;
    target.setAttribute('aria-label', `Calibration target ${index + 1}`);
    target.addEventListener('click', (event) => {
      calibrationClicks += 1;
      const rect = event.currentTarget.getBoundingClientRect();
      const x = rect.left + rect.width / 2;
      const y = rect.top + rect.height / 2;
      if (window.webgazer?.recordScreenPosition) {
        window.webgazer.recordScreenPosition(x, y, 'click');
      }
      logEvent('calibration_click', `${index + 1}`, { gaze_x: x.toFixed(2), gaze_y: y.toFixed(2) });
      event.currentTarget.classList.remove('active-target');
      const next = calibrationArea.querySelectorAll('.target')[calibrationClicks];
      if (next) {
        next.classList.add('active-target');
      } else {
        startReading();
      }
    });
    calibrationArea.appendChild(target);
  });
}

async function startWebGazer() {
  if (!window.webgazer) {
    throw new Error('WebGazer did not load. Check network access to the WebGazer script.');
  }
  const webgazer = window.webgazer;

  if (webgazer.params) {
    webgazer.params.faceMeshSolutionPath = './mediapipe/face_mesh';
    webgazer.params.showVideo = false;
    webgazer.params.showVideoPreview = false;
    webgazer.params.showFaceOverlay = false;
    webgazer.params.showFaceFeedbackBox = false;
    webgazer.params.showGazeDot = false;
  }

  webgazer.setGazeListener(logGaze);
  ['showVideo', 'showVideoPreview', 'showFaceOverlay', 'showFaceFeedbackBox', 'showPredictionPoints'].forEach((methodName) => {
    if (typeof webgazer[methodName] === 'function') {
      webgazer[methodName](false);
    }
  });

  const beginResult = webgazer.begin();
  if (beginResult && typeof beginResult.then === 'function') {
    await beginResult;
  }
}

function startReading() {
  currentPassage = 0;
  renderPassage();
  showPanel('reading');
  setStatus('Reading task running');
}

function renderPassage() {
  currentTrialId = `trial_${currentPassage + 1}`;
  passageCounter.textContent = `Passage ${currentPassage + 1} / ${passages.length}`;
  passageText.textContent = passages[currentPassage].text;
  logEvent('passage_show', passages[currentPassage].id);
}

function renderQuiz() {
  quizItems.innerHTML = '';
  quiz.forEach((item, index) => {
    const wrapper = document.createElement('div');
    wrapper.className = 'quiz-item';
    const label = document.createElement('label');
    label.textContent = item.question;
    const select = document.createElement('select');
    select.id = item.id;
    item.options.forEach((option) => {
      const optionEl = document.createElement('option');
      optionEl.value = option;
      optionEl.textContent = option;
      select.appendChild(optionEl);
    });
    label.appendChild(select);
    wrapper.appendChild(label);
    quizItems.appendChild(wrapper);
    logEvent('quiz_item_show', `${index + 1}`);
  });
}

function exportCsv() {
  logEvent('export', 'csv');
  const headers = Object.keys(baseRow('header'));
  const escapeCsv = (value) => {
    const text = String(value ?? '');
    return /[",\n]/.test(text) ? `"${text.replace(/"/g, '""')}"` : text;
  };
  const csv = [headers.join(',')].concat(rows.map((row) => headers.map((header) => escapeCsv(row[header])).join(','))).join('\n');
  const blob = new Blob([csv], { type: 'text/csv;charset=utf-8' });
  const link = document.createElement('a');
  link.href = URL.createObjectURL(blob);
  link.download = `reading_gaze_${participantId}_${sessionId}.csv`;
  document.body.appendChild(link);
  link.click();
  link.remove();
  URL.revokeObjectURL(link.href);
}

startBtn.addEventListener('click', async () => {
  try {
    participantId = participantInput.value.trim() || 'P001';
    startBtn.disabled = true;
    setStatus('Starting camera and WebGazer');
    await startWebGazer();
    started = true;
    buildCalibrationTargets();
    showPanel('calibration');
    setStatus('Calibration');
  } catch (error) {
    console.error(error);
    startBtn.disabled = false;
    setStatus(`WebGazer start failed: ${error.message || error}`);
  }
});

continueBtn.addEventListener('click', () => {
  showPanel('probe');
  setStatus('Probe');
});

probeSubmitBtn.addEventListener('click', () => {
  const tut = document.getElementById('tutAnswer').value;
  const difficulty = document.getElementById('difficulty').value;
  const familiarity = document.getElementById('familiarity').value;
  logEvent('probe_answer', `trial_${currentPassage + 1}`, {
    probe_tut: tut,
    difficulty,
    familiarity
  });
  currentPassage += 1;
  if (currentPassage < passages.length) {
    renderPassage();
    showPanel('reading');
    setStatus('Reading task running');
  } else {
    currentTrialId = 'quiz';
    renderQuiz();
    showPanel('quiz');
    setStatus('Comprehension');
  }
});

quizSubmitBtn.addEventListener('click', () => {
  quiz.forEach((item) => {
    const answer = document.getElementById(item.id).value;
    logEvent('quiz_answer', item.id, {
      comprehension_correct: answer === item.answer ? '1' : '0'
    });
  });
  exportBtn.disabled = false;
  showPanel('done');
  setStatus('Complete');
  if (window.webgazer?.pause) {
    window.webgazer.pause();
  }
});

exportBtn.addEventListener('click', exportCsv);
