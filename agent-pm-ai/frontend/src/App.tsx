import { useState } from "react";

function App() {
  const [input, setInput] = useState("");
  const [output, setOutput] = useState<any>(null);

  const handleSubmit = async () => {
    const res = await fetch("http://localhost:8000/generate", {
      method: "POST",
      headers: {"Content-Type": "application/json"},
      body: JSON.stringify({ prompt: input }),
    });
    const data = await res.json();
    setOutput(data.result);
  };

  return (
    <div style={{ padding: 20 }}>
      <h1>Agent PM AI</h1>
      <input value={input} onChange={(e) => setInput(e.target.value)} />
      <button onClick={handleSubmit}>Generate</button>
      <pre>{JSON.stringify(output, null, 2)}</pre>
    </div>
  );
}

export default App;
