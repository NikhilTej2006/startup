import {Routes, Route} from "react-router-dom";
import Landing from "./pages/Landing";
import Validate from "./pages/Validate";
import Dashboard from "./pages/Dashboard";
import Report from "./pages/Report";

export default function App() {
  return(
    <Routes>
      <Route path="/" element = {<Landing />} />
      <Route path="/validate" element={<Validate />}/>
      <Route path="/dashboard" element={<Dashboard />}/>
      <Route path="/report" element={<Report />}/>
    </Routes>
  )
}
