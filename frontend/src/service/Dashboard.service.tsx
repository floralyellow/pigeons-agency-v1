class DashboardService {
  headers = new Headers({
    Accept: "application/json",
    "Content-Type": "application/json"
  });
  testBackend = async () => {
    const test = await fetch("http://localhost/api/test/", {
      method: "GET",
      headers: this.headers,
      cache: "default"
    });
    const testJson = await test.json();
    if(testJson && testJson.status)
      return testJson.status ;
  }
}
export default DashboardService;