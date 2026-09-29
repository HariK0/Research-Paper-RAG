const apiBaseUrl = import.meta.env.VITE_API_BASE_URL ?? 'http://localhost:8000'

export default function App() {
  return (
    <main className="shell">
      <div className="eyebrow"><span className="status-dot" /> RESEARCH WORKSPACE</div>
      <h1>Understand the papers<br />behind the <em>ideas.</em></h1>
      <p className="intro">Your research assistant is taking shape. Soon, you’ll be able to bring your papers together and ask better questions of them.</p>
      <section className="setup-card" aria-label="Project status">
        <div className="card-mark">R</div>
        <div><strong>Workspace ready to grow</strong><p>Project foundation is running. Paper ingestion and grounded answers come next.</p></div>
        <a href={`${apiBaseUrl}/docs`} target="_blank" rel="noreferrer">API docs ↗</a>
      </section>
      <footer>BUILT FOR CURIOUS MINDS <span>·</span> PHASE 01</footer>
    </main>
  )
}
