import { Component } from 'react';
import './Dashboard.css';
import DashboardService  from '../../service/Dashboard.service';

class Dashboard extends Component {
  test :any;
  constructor(props = [],public service = new DashboardService){
    super(props);
  }
  componentWillMount(){
    this.test = this.service.testBackend;
  }
  render(): JSX.Element{
    return (
      <div className="Dashboard">
        <p className="Dashboard-intro">
          From backend: { this.test}
        </p>
      </div>
    );
  }
}
export default Dashboard;
