"""HTML templates for the built-in dashboard."""

from __future__ import annotations

INDEX_HTML = """
<!doctype html>
<html lang="en">
<head>
  <meta charset="utf-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1" />
  <meta name="description" content="Compile requirements into secure runnable project scaffolds." />
  <title>Universal Project Compiler Agent</title>
  <script defer src="https://cdn.vercel-insights.com/v1/script.js"></script>
  <style>
    :root {
      color-scheme: dark;
      --bg: #070a12;
      --panel: #0f172a;
      --panel-soft: #111827;
      --text: #f8fafc;
      --muted: #94a3b8;
      --line: rgba(255, 255, 255, 0.12);
      --accent: #8b5cf6;
      --accent-2: #06b6d4;
      --success: #22c55e;
      --danger: #fb7185;
      --shadow: 0 24px 80px rgba(0, 0, 0, 0.42);
    }
    * { box-sizing: border-box; }
    body {
      margin: 0;
      min-height: 100vh;
      font-family: Inter, ui-sans-serif, system-ui, -apple-system, BlinkMacSystemFont, sans-serif;
      background:
        radial-gradient(circle at 16% 0%, rgba(139, 92, 246, 0.32), transparent 34rem),
        radial-gradient(circle at 92% 12%, rgba(6, 182, 212, 0.22), transparent 28rem),
        var(--bg);
      color: var(--text);
    }
    main { width: min(1180px, 100%); margin: auto; padding: clamp(20px, 4vw, 64px); }
    .nav { display: flex; justify-content: space-between; align-items: center; gap: 16px; margin-bottom: 56px; }
    .brand { display: flex; align-items: center; gap: 12px; color: var(--muted); font-weight: 700; }
    .logo { width: 36px; height: 36px; border-radius: 12px; background: linear-gradient(135deg, var(--accent), var(--accent-2)); box-shadow: 0 0 40px rgba(139, 92, 246, 0.45); }
    .pill { border: 1px solid var(--line); border-radius: 999px; padding: 9px 13px; color: var(--muted); background: rgba(255, 255, 255, 0.06); }
    .hero { display: grid; grid-template-columns: minmax(0, 1.05fr) minmax(320px, 0.95fr); gap: clamp(24px, 5vw, 56px); align-items: start; }
    h1 { font-size: clamp(44px, 7vw, 84px); line-height: 0.95; letter-spacing: -0.07em; margin: 0; }
    .lead { color: var(--muted); font-size: clamp(17px, 2vw, 21px); line-height: 1.65; max-width: 760px; }
    .features { display: grid; grid-template-columns: repeat(auto-fit, minmax(180px, 1fr)); gap: 12px; margin-top: 28px; }
    .feature, .workspace { border: 1px solid var(--line); border-radius: 26px; background: linear-gradient(180deg, rgba(255, 255, 255, 0.09), rgba(255, 255, 255, 0.04)); box-shadow: var(--shadow); }
    .feature { padding: 18px; color: var(--muted); }
    .feature strong { display: block; color: var(--text); margin-bottom: 6px; }
    .workspace { padding: clamp(18px, 3vw, 28px); position: relative; overflow: hidden; }
    .workspace::before { content: ""; position: absolute; inset: 0; background: radial-gradient(circle at top right, rgba(139, 92, 246, 0.16), transparent 20rem); pointer-events: none; }
    form, .result { position: relative; display: grid; gap: 14px; }
    label { color: var(--muted); font-size: 14px; font-weight: 700; }
    input, textarea { width: 100%; border: 1px solid var(--line); border-radius: 16px; padding: 13px 14px; background: rgba(2, 6, 23, 0.7); color: var(--text); outline: none; }
    textarea { min-height: 190px; resize: vertical; line-height: 1.5; }
    input:focus, textarea:focus { border-color: rgba(139, 92, 246, 0.9); box-shadow: 0 0 0 4px rgba(139, 92, 246, 0.18); }
    .actions { display: flex; flex-wrap: wrap; gap: 10px; }
    button { border: 0; border-radius: 999px; padding: 12px 16px; color: white; font-weight: 800; cursor: pointer; background: linear-gradient(135deg, var(--accent), var(--accent-2)); transition: transform .18s ease, filter .18s ease; }
    button.secondary { background: rgba(255, 255, 255, 0.08); border: 1px solid var(--line); }
    button:hover { transform: translateY(-1px); filter: brightness(1.08); }
    button:disabled { cursor: progress; opacity: .7; transform: none; }
    .result { margin-top: 18px; padding-top: 18px; border-top: 1px solid var(--line); }
    .status { min-height: 24px; color: var(--muted); }
    .status.ok { color: var(--success); }
    .status.err { color: var(--danger); }
    pre { margin: 0; overflow: auto; max-height: 360px; border: 1px solid var(--line); border-radius: 18px; padding: 16px; background: rgba(2, 6, 23, 0.78); color: #dbeafe; }
    @media (max-width: 860px) {
      .hero { grid-template-columns: 1fr; }
      .nav { align-items: flex-start; flex-direction: column; margin-bottom: 34px; }
      h1 { letter-spacing: -0.05em; }
    }
  </style>
</head>
<body>
<main>
  <nav class="nav" aria-label="Primary">
    <div class="brand"><span class="logo" aria-hidden="true"></span> Universal Project Compiler Agent</div>
    <div class="pill">Termux-first • Secure scaffold • FastAPI</div>
  </nav>
  <section class="hero">
    <div>
      <h1>Turn rough specs into runnable software projects.</h1>
      <p class="lead">Analyze requirements, receive a prioritized implementation plan, then generate a clean scaffold with docs, tests, scripts, security defaults, and mobile-friendly workflows.</p>
      <div class="features">
        <div class="feature"><strong>Plan</strong>Critical/High/Medium/Low tasks with impact and file scope.</div>
        <div class="feature"><strong>Compile</strong>Safe project generation with secret redaction and path checks.</div>
        <div class="feature"><strong>Ship</strong>Termux-friendly setup, start, update, backup, tests, and CI.</div>
      </div>
    </div>
    <div class="workspace">
      <form id="compiler-form">
        <label for="project_name">Project name</label>
        <input id="project_name" name="project_name" maxlength="120" placeholder="CRM Dashboard" />
        <label for="requirements">Requirements</label>
        <textarea id="requirements" name="requirements" required maxlength="100000"># CRM Dashboard
Need auth, API, admin dashboard, dark mode, responsive UI, and deployment scripts.</textarea>
        <div class="actions">
          <button type="button" id="plan-btn">Generate plan</button>
          <button type="button" id="compile-btn" class="secondary">Compile scaffold</button>
        </div>
      </form>
      <div class="result" aria-live="polite">
        <div id="status" class="status">Ready.</div>
        <pre id="output">{}</pre>
      </div>
    </div>
  </section>
</main>
<script>
  const form = document.querySelector('#compiler-form');
  const statusNode = document.querySelector('#status');
  const outputNode = document.querySelector('#output');
  const planButton = document.querySelector('#plan-btn');
  const compileButton = document.querySelector('#compile-btn');

  function payload() {
    const data = new FormData(form);
    return {
      project_name: data.get('project_name') || null,
      requirements: data.get('requirements') || ''
    };
  }

  async function submit(endpoint, button) {
    statusNode.className = 'status';
    statusNode.textContent = 'Working...';
    planButton.disabled = true;
    compileButton.disabled = true;
    try {
      const response = await fetch(endpoint, {
        method: 'POST',
        headers: { 'content-type': 'application/json' },
        body: JSON.stringify(payload())
      });
      const body = await response.json();
      if (!response.ok) throw new Error(body.detail || 'Request failed');
      outputNode.textContent = JSON.stringify(body, null, 2);
      statusNode.className = 'status ok';
      statusNode.textContent = endpoint.includes('compile') ? 'Scaffold generated.' : 'Plan generated.';
    } catch (error) {
      statusNode.className = 'status err';
      statusNode.textContent = error.message;
    } finally {
      planButton.disabled = false;
      compileButton.disabled = false;
    }
  }

  planButton.addEventListener('click', () => submit('/api/plan', planButton));
  compileButton.addEventListener('click', () => submit('/api/compile', compileButton));
</script>
</body>
</html>
"""
