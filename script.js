const taskForm = document.querySelector('#taskForm');
const taskInput = document.querySelector('#taskInput');
const taskList = document.querySelector('#taskList');
const emptyState = document.querySelector('#emptyState');
const taskCount = document.querySelector('#taskCount');
const progressValue = document.querySelector('#progressValue');
const today = document.querySelector('#today');
let tasks = JSON.parse(localStorage.getItem('taskline-tasks') || '[]');
let currentFilter = 'all';

today.textContent = new Intl.DateTimeFormat('en', { weekday: 'short', month: 'short', day: 'numeric' }).format(new Date());

taskForm.addEventListener('submit', (event) => {
  event.preventDefault();
  const title = taskInput.value.trim();
  if (!title) return;
  tasks.unshift({ id: crypto.randomUUID(), title, completed: false });
  taskInput.value = '';
  persistAndRender();
});

document.querySelectorAll('.filter').forEach((button) => {
  button.addEventListener('click', () => {
    currentFilter = button.dataset.filter;
    document.querySelectorAll('.filter').forEach((item) => item.classList.toggle('active', item === button));
    render();
  });
});

taskList.addEventListener('change', (event) => {
  const task = tasks.find((item) => item.id === event.target.dataset.id);
  if (task) task.completed = event.target.checked;
  persistAndRender();
});

taskList.addEventListener('click', (event) => {
  if (!event.target.matches('.delete-task')) return;
  tasks = tasks.filter((item) => item.id !== event.target.dataset.id);
  persistAndRender();
});

function persistAndRender() {
  localStorage.setItem('taskline-tasks', JSON.stringify(tasks));
  render();
}

function render() {
  const visibleTasks = tasks.filter((task) => currentFilter === 'all' || (currentFilter === 'active' && !task.completed) || (currentFilter === 'completed' && task.completed));
  taskList.innerHTML = visibleTasks.map((task) => `<li class="task-item ${task.completed ? 'completed' : ''}"><input type="checkbox" data-id="${task.id}" ${task.completed ? 'checked' : ''} aria-label="Mark ${escapeHtml(task.title)} complete"><span class="task-text">${escapeHtml(task.title)}</span><button class="delete-task" data-id="${task.id}" type="button" aria-label="Delete ${escapeHtml(task.title)}">Delete</button></li>`).join('');
  emptyState.hidden = visibleTasks.length > 0;
  taskCount.textContent = `${tasks.length} ${tasks.length === 1 ? 'task' : 'tasks'}`;
  const completedCount = tasks.filter((task) => task.completed).length;
  progressValue.textContent = `${tasks.length ? Math.round((completedCount / tasks.length) * 100) : 0}%`;
}

function escapeHtml(value) {
  return value.replace(/[&<>'"]/g, (character) => ({ '&': '&amp;', '<': '&lt;', '>': '&gt;', "'": '&#39;', '"': '&quot;' }[character]));
}

render();
