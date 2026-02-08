import { useState } from "react";
import { api } from "../api/api";

export default function EmployeeForm() {
  const [form, setForm] = useState({});

  const submit = async () => {
    await api.post("/employees", form);
    window.location.reload();
  };

  return (
    <div className="bg-white p-5 rounded shadow">
      <h2 className="font-semibold mb-4">Add Employee</h2>

      {["employee_id","full_name","email","department"].map(f => (
        <input
          key={f}
          placeholder={f.replace("_"," ").toUpperCase()}
          className="w-full mb-3 p-2 border rounded"
          onChange={e => setForm({...form, [f]: e.target.value})}
        />
      ))}

      <button
        onClick={submit}
        className="bg-blue-600 text-white px-4 py-2 rounded"
      >
        Add Employee
      </button>
    </div>
  );
}