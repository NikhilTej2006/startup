import {Routes, Route, BrowserRouter} from "react-router-dom";
import Landing from "./pages/Landing";
import Validate from "./pages/Validate";
import Dashboard from "./pages/Dashboard";
import Report from "./pages/Report";
import Market from "./pages/Market";
import Swot from "./pages/swot";

export default function App() {
  return(
    <Routes>
      <Route path="/" element = {<Landing />} />
      <Route path="/validate" element={<Validate />}/>
      <Route path="/dashboard" element={<Dashboard />}/>
      <Route path="/report" element={<Report />}/>
      <Route path="/market" element={<Market />}/>
      <Route path="/swot" element={<Swot />} />
    </Routes>
  )
}
