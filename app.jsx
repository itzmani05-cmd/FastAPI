import { useState, useEffect } from "react";

function App() {
  const [message, setMessage] = useState("Nothing");

  useEffect(() => {
    fetch("http://127.0.0.1:8000/message")
      .then(response => response.json())
      .then(data => { console.log(data);
        setMessage(data.message); })
      .catch(error => console.error("Error:", error));
  }, []);

  return (
    <div>
      <h1>FastAPI + React</h1>
      <p>{message}</p>
    </div>
  );
}

export default App;
