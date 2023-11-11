import logo from './logo.svg';
import './App.css';
import './ComponentsfirstPage/gameButtonComponent'
import ButtonsMenu from "./ComponentsfirstPage/selectGameComponent"
import'./ComponentsfirstPage/levelButtonsComponent'
import SudokuBoard from "./ComponentsSecondPage/SudokuBoardComponent";
function App() {
  return (
    <div className="App">
      <header className="App-header">
          <h1>PENTRU LUMI</h1>
          <ButtonsMenu/>
          <SudokuBoard></SudokuBoard>

      </header>

    </div>
  );
}

export default App;
