class TaskAPI {
    constructor(baseURL) {
        this.baseURL = baseURL;
    }

    async createTask(title, description) {
        const response = await fetch(`${this.baseURL}/tasks`, {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify({ title, description })
        });
        return response.json();
    }

    async getTasks() {
        const response = await fetch(`${this.baseURL}/tasks`);
        return response.json();
    }

    async updateTask(id, updates) {
        const response = await fetch(`${this.baseURL}/tasks/${id}`, {
            method: 'PUT',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify(updates)
        });
        return response.json();
    }

    async deleteTask(id) {
        await fetch(`${this.baseURL}/tasks/${id}`, {
            method: 'DELETE'
        });
    }
}

// Cliente React para o serviço
import React, { useState, useEffect } from 'react';

const TaskManager = () => {
    const [tasks, setTasks] = useState([]);
    const [title, setTitle] = useState('');
    const [description, setDescription] = useState('');

    const api = new TaskAPI('http://localhost:3000');

    useEffect(() => {
        api.getTasks().then(setTasks);
    }, []);

    const handleAddTask = async () => {
        const newTask = await api.createTask(title, description);
        setTasks([...tasks, newTask]);
        setTitle('');
        setDescription('');
    };

    const handleUpdateTask = async (id, completed) => {
        const updatedTask = await api.updateTask(id, { completed });
        setTasks(tasks.map(t => (t.id === id ? updatedTask : t)));
    };

    const handleDeleteTask = async (id) => {
        await api.deleteTask(id);
        setTasks(tasks.filter(t => t.id !== id));
    };

    return (
        <div>
            <h1>Task Manager</h1>
            <input
                type="text"
                placeholder="Title"
                value={title}
                onChange={(e) => setTitle(e.target.value)}
            />
            <input
                type="text"
                placeholder="Description"
                value={description}
                onChange={(e) => setDescription(e.target.value)}
            />
            <button onClick={handleAddTask}>Add Task</button>
            <ul>
                {tasks.map(task => (
                    <li key={task.id}>
                        <h3>{task.title}</h3>
                        <p>{task.description}</p>
                        <p>Status: {task.completed ? 'Completed' : 'Pending'}</p>
                        <button onClick={() => handleUpdateTask(task.id, !task.completed)}>
                            {task.completed ? 'Mark as Pending' : 'Mark as Completed'}
                        </button>
                        <button onClick={() => handleDeleteTask(task.id)}>Delete</button>
                    </li>
                ))}
            </ul>
        </div>
    );
};

export default TaskManager;