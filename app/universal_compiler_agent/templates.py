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
  <style>
    :root {
      color-scheme: dark;
      --bg: #050714;
      --panel: rgba(15, 23, 42, 0.78);
      --panel-strong: rgba(15, 23, 42, 0.94);
      --text: #f8fafc;
      --muted: #9fb1d1;
      --line: rgba(255, 255, 255, 0.14);
      --accent: #8b5cf6;
      --accent-2: #06b6d4;
      --accent-3: #22c55e;
      --danger: #fb7185;
      --shadow: 0 28px 90px rgba(0, 0, 0, 0.44);
    }
    * { box-sizing: border-box; }
    html { scroll-behavior: smooth; }
    body {
      margin: 0;
      min-height: 100vh;
      font-family: Inter, ui-sans-serif, system-ui, -apple-system, BlinkMacSystemFont, sans-serif;
      background:
        radial-gradient(circle at 18% 2%, rgba(139, 92, 246, 0.34), transparent 31rem),
        radial-gradient(circle at 92% 10%, rgba(6, 182, 212, 0.25), transparent 30rem),
        radial-gradient(circle at 58% 110%, rgba(34, 197, 94, 0.14), transparent 34rem),
        var(--bg);
      color: var(--text);
      overflow-x: hidden;
    }
    body::before {
      animation: drift 18s linear infinite;
      background-image: linear-gradient(rgba(255, 255, 255, 0.04) 1px, transparent 1px), linear-gradient(90deg, rgba(255, 255, 255, 0.04) 1px, transparent 1px);
      background-size: 72px 72px;
      content: "";
      inset: -20%;
      mask-image: radial-gradient(circle at center, black, transparent 72%);
      pointer-events: none;
      position: fixed;
      z-index: -1;
    }
    main { width: min(1180px, 100%); margin: auto; padding: clamp(20px, 4vw, 64px); }
    .nav { align-items: center; display: flex; gap: 16px; justify-content: space-between; margin-bottom: 52px; }
    .brand { align-items: center; color: var(--muted); display: flex; font-weight: 800; gap: 12px; letter-spacing: .01em; }
    .logo { animation: pulse 3s ease-in-out infinite; background: linear-gradient(135deg, var(--accent), var(--accent-2)); border-radius: 14px; box-shadow: 0 0 44px rgba(139, 92, 246, 0.5); height: 38px; width: 38px; }
    .nav-links { display: flex; flex-wrap: wrap; gap: 10px; justify-content: flex-end; }
    .pill, .badge { align-items: center; border: 1px solid var(--line); border-radius: 999px; color: var(--muted); display: inline-flex; gap: 8px; padding: 9px 13px; text-decoration: none; }
    .pill { background: rgba(255, 255, 255, 0.06); }
    .badge { background: rgba(2, 6, 23, 0.54); font-size: 13px; font-weight: 800; }
    .badge::before { background: var(--accent-3); border-radius: 999px; box-shadow: 0 0 18px var(--accent-3); content: ""; height: 8px; width: 8px; }
    .hero { align-items: start; display: grid; gap: clamp(24px, 5vw, 58px); grid-template-columns: minmax(0, 1.02fr) minmax(320px, 0.98fr); }
    .eyebrow { color: #67e8f9; font-size: 13px; font-weight: 900; letter-spacing: .22em; margin: 0 0 18px; text-transform: uppercase; }
    h1 { font-size: clamp(46px, 7vw, 90px); letter-spacing: -0.075em; line-height: .92; margin: 0; max-width: 820px; }
    .gradient { background: linear-gradient(90deg, #fff, #c4b5fd 45%, #67e8f9); -webkit-background-clip: text; color: transparent; }
    .lead { color: var(--muted); font-size: clamp(17px, 2vw, 22px); line-height: 1.68; margin: 24px 0 0; max-width: 760px; }
    .hero-actions { display: flex; flex-wrap: wrap; gap: 12px; margin-top: 30px; }
    .cta { background: linear-gradient(135deg, var(--accent), var(--accent-2)); border-radius: 999px; box-shadow: 0 18px 50px rgba(6, 182, 212, .24); color: white; font-weight: 900; padding: 13px 17px; text-decoration: none; }
    .cta.secondary { background: rgba(255, 255, 255, 0.08); border: 1px solid var(--line); box-shadow: none; color: var(--text); }
    .stats, .features, .deploy-grid { display: grid; gap: 12px; }
    .stats { grid-template-columns: repeat(3, minmax(0, 1fr)); margin-top: 34px; }
    .stat, .feature, .workspace, .deploy-card, .terminal { backdrop-filter: blur(20px); background: linear-gradient(180deg, rgba(255, 255, 255, 0.095), rgba(255, 255, 255, 0.04)); border: 1px solid var(--line); border-radius: 26px; box-shadow: var(--shadow); }
    .stat { padding: 18px; }
    .stat strong { display: block; font-size: 28px; letter-spacing: -.04em; }
    .stat span, .feature, .deploy-card p { color: var(--muted); }
    .features { grid-template-columns: repeat(auto-fit, minmax(178px, 1fr)); margin-top: 18px; }
    .feature { padding: 18px; }
    .feature strong { color: var(--text); display: block; margin-bottom: 6px; }
    .workspace { overflow: hidden; padding: clamp(18px, 3vw, 28px); position: relative; }
    .workspace::before { background: radial-gradient(circle at top right, rgba(139, 92, 246, 0.18), transparent 20rem); content: ""; inset: 0; pointer-events: none; position: absolute; }
    .orbit { aspect-ratio: 1; border: 1px solid rgba(255, 255, 255, .12); border-radius: 999px; inset: auto -64px -86px auto; opacity: .62; position: absolute; width: 220px; }
    .orbit::after { animation: orbit 7s linear infinite; background: linear-gradient(135deg, var(--accent-2), var(--accent-3)); border-radius: 999px; box-shadow: 0 0 26px rgba(34, 197, 94, .8); content: ""; height: 16px; left: 50%; position: absolute; top: -8px; transform-origin: 0 118px; width: 16px; }
    form, .result { display: grid; gap: 14px; position: relative; }
    label { color: var(--muted); font-size: 14px; font-weight: 800; }
    input, textarea { background: rgba(2, 6, 23, .72); border: 1px solid var(--line); border-radius: 16px; color: var(--text); outline: none; padding: 13px 14px; width: 100%; }
    textarea { line-height: 1.5; min-height: 190px; resize: vertical; }
    input:focus, textarea:focus { border-color: rgba(139, 92, 246, .9); box-shadow: 0 0 0 4px rgba(139, 92, 246, .18); }
    .actions { display: flex; flex-wrap: wrap; gap: 10px; }
    button { background: linear-gradient(135deg, var(--accent), var(--accent-2)); border: 0; border-radius: 999px; color: white; cursor: pointer; font-weight: 900; padding: 12px 16px; transition: transform .18s ease, filter .18s ease; }
    button.secondary { background: rgba(255, 255, 255, .08); border: 1px solid var(--line); }
    button:hover { filter: brightness(1.08); transform: translateY(-1px); }
    button:disabled { cursor: progress; opacity: .7; transform: none; }
    .result { border-top: 1px solid var(--line); margin-top: 18px; padding-top: 18px; }
    .status { color: var(--muted); min-height: 24px; }
    .status.ok { color: var(--accent-3); }
    .status.err { color: var(--danger); }
    pre { background: rgba(2, 6, 23, .78); border: 1px solid var(--line); border-radius: 18px; color: #dbeafe; margin: 0; max-height: 360px; overflow: auto; padding: 16px; }
    .section { margin-top: clamp(46px, 8vw, 86px); }
    .section h2 { font-size: clamp(30px, 4vw, 52px); letter-spacing: -.05em; margin: 0 0 12px; }
    .section > p { color: var(--muted); line-height: 1.7; margin: 0 0 22px; max-width: 760px; }
    .deploy-grid { grid-template-columns: repeat(auto-fit, minmax(230px, 1fr)); }
    .deploy-card { padding: 22px; }
    .deploy-card strong { display: block; font-size: 18px; margin-bottom: 9px; }
    .terminal { background: rgba(2, 6, 23, .86); margin-top: 18px; overflow: hidden; }
    .terminal-bar { align-items: center; border-bottom: 1px solid var(--line); display: flex; gap: 7px; padding: 12px 14px; }
    .dot { border-radius: 999px; height: 11px; width: 11px; }
    .dot:nth-child(1) { background: #fb7185; } .dot:nth-child(2) { background: #facc15; } .dot:nth-child(3) { background: #22c55e; }
    .terminal code { color: #bfdbfe; display: block; line-height: 1.7; padding: 18px; white-space: pre-wrap; }
    @keyframes drift { to { transform: translate3d(72px, 72px, 0); } }
    @keyframes pulse { 50% { transform: scale(1.08) rotate(6deg); } }
    @keyframes orbit { to { transform: rotate(360deg); } }
    @media (max-width: 860px) {
      .hero { grid-template-columns: 1fr; }
      .nav { align-items: flex-start; flex-direction: column; margin-bottom: 34px; }
      .stats { grid-template-columns: 1fr; }
      h1 { letter-spacing: -0.055em; }
    }
  </style>
</head>
<body>
<main>
  <nav class="nav" aria-label="Primary">
    <div class="brand"><span class="logo" aria-hidden="true"></span> Universal Project Compiler Agent</div>
    <div class="nav-links">
      <a class="pill" href="/docs">API docs</a>
      <a class="pill" href="https://github.com/Huynhthuongg/AGENTS.md">GitHub</a>
      <span class="badge">Vercel-ready</span>
    </div>
  </nav>
  <section class="hero">
    <div>
      <p class="eyebrow">Android-first • Termux-first • Serverless-ready</p>
      <h1>Compile rough specs into <span class="gradient">ship-ready projects.</span></h1>
      <p class="lead">Analyze requirements, produce a prioritized implementation plan, and generate a clean scaffold with docs, tests, scripts, security defaults, and mobile-friendly workflows.</p>
      <div class="hero-actions">
        <a class="cta" href="#compiler-form">Try the compiler</a>
        <a class="cta secondary" href="/openapi.json">OpenAPI schema</a>
      </div>
      <div class="stats" aria-label="Project highlights">
        <div class="stat"><strong>3</strong><span>interfaces: CLI, API, dashboard</span></div>
        <div class="stat"><strong>4</strong><span>priority levels for task planning</span></div>
        <div class="stat"><strong>0</strong><span>Docker required for Termux use</span></div>
      </div>
      <div class="features">
        <div class="feature"><strong>Plan</strong>Critical/High/Medium/Low tasks with impact and file scope.</div>
        <div class="feature"><strong>Compile</strong>Safe project generation with secret redaction and path checks.</div>
        <div class="feature"><strong>Ship</strong>Termux-friendly setup, start, update, backup, tests, CI, and Vercel deployment.</div>
      </div>
    </div>
    <div class="workspace">
      <div class="orbit" aria-hidden="true"></div>
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
  <section class="section" aria-labelledby="deploy-title">
    <h2 id="deploy-title">Built for fast release paths.</h2>
    <p>The project now includes the pieces a public project page needs: live API docs, a hands-on compiler form, GitHub badges, CI checks, and Vercel serverless deployment wiring.</p>
    <div class="deploy-grid">
      <div class="deploy-card"><strong>GitHub-ready</strong><p>README badges advertise CI, Python, FastAPI, Vercel readiness, license, and release version.</p></div>
      <div class="deploy-card"><strong>Vercel-ready</strong><p>A lightweight ASGI entrypoint and runtime config route every request to the FastAPI app.</p></div>
      <div class="deploy-card"><strong>Termux-ready</strong><p>Local scripts stay minimal for Android devices with limited memory and storage.</p></div>
    </div>
    <div class="terminal" aria-label="Release commands">
      <div class="terminal-bar"><span class="dot"></span><span class="dot"></span><span class="dot"></span></div>
      <code>$ python -m pip install -e '.[dev]'
$ ./scripts/check.sh
$ vercel deploy --prod</code>
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

  async function submit(endpoint) {
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

  planButton.addEventListener('click', () => submit('/plan'));
  compileButton.addEventListener('click', () => submit('/compile'));
</script>
</body>
</html>
"""
