import { Component } from 'react';
import './Login.css';
import DashboardService  from '../../service/Dashboard.service';

class Login extends Component {
  test :any;
  constructor(props = [],public service = new DashboardService){
    super(props);
  }
  componentWillMount(){
    this.test = this.service.testBackend;
  }
  render(): JSX.Element{
    return (
      <div className="Login">
        <p className="Login-intro">
          From backend: { this.test}
        </p>
      </div>
    );
  }
}
export default Login;
