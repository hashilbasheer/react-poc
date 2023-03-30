import './App.css';

function App() {
  return (
    <div className="App">
      <header className="App-header">
        <p>
          Welcome to VOLVO SALES COCKPIT !! The Build Number is : {process.env.GITHUB_RUN_NUMBER}
        </p>
      </header>
    </div>
  );
}

export default App;
