
const express = require('express');
const app = express();
app.use(express.json());


let tasks = [];
let idCounter = 1;


app.post('/tasks', (req, res) => {
    const { title, description } = req.body;
    const newTask = { id: idCounter++, title, description, completed: false };
    tasks.push(newTask);
    res.status(201).json(newTask);
});


app.get('/tasks', (req, res) => {
    res.json(tasks);
});


app.put('/tasks/:id', (req, res) => {
    const { id } = req.params;
    const { title, description, completed } = req.body;
    const task = tasks.find(t => t.id === parseInt(id));

    if (!task) {
        return res.status(404).json({ message: 'Task not found' });
    }

    if (title) task.title = title;
    if (description) task.description = description;
    if (completed !== undefined) task.completed = completed;

    res.json(task);
});


app.delete('/tasks/:id', (req, res) => {
    const { id } = req.params;
    tasks = tasks.filter(t => t.id !== parseInt(id));
    res.status(204).send();
});

app.listen(3000, () => console.log('Service running on http://localhost:3000'));
