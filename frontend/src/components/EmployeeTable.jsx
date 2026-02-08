import { useEffect, useState } from "react";
import { api } from "../api/api";

export default function EmployeeTable() {
  const [employees, setEmployees] = useState([]);

  useEffect(() => {
    api.get("/employees").then(res => setEmployees(res.data));
  }, []);

  return (
    <div className="bg-white p-5 rounded shadow">
      <h2 className="font-semibold mb-4">Employees</h2>

      <table className="w-full border">
        <thead className="bg-gray-200">
          <tr>
            <th className="p-2">Name</th>
            <th>Department</th>
            <th>Email</th>
          </tr>
        </thead>
        <tbody>
          {employees.map(e => (
            <tr key={e.id} className="border-t">
              <td className="p-2">{e.full_name}</td>
              <td>{e.department}</td>
              <td>{e.email}</td>
            </tr>
          ))}
        </tbody>
      </table>
    </div>
  );
}