import EmployeeForm from "../components/EmployeeForm";
import EmployeeTable from "../components/EmployeeTable";

export default function Dashboard() {
  return (
    <div className="max-w-6xl mx-auto p-6">
      <h1 className="text-3xl font-bold mb-6">HRMS Lite</h1>

      <div className="grid md:grid-cols-2 gap-6">
        <EmployeeForm />
        <EmployeeTable />
      </div>
    </div>
  );
}