import { Component } from 'react';
import './Register.css';
import DashboardService  from '../../service/Dashboard.service';

class Register extends Component {
  test :any;
  constructor(props = [],public service = new DashboardService){
    super(props);
  }
  componentWillMount(){
    this.test = this.service.testBackend;
  }
  render(): JSX.Element{
    return (
      <div className="Register">
        <p className="Register-intro">
          From backend: { this.test}
        </p>
      </div>
    );
  }
}
export default Register;
