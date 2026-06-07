const form = document.getElementById('userForm');

const userList = document.getElementById('userList');

form.addEventListener('submit', async function(event) {

event.preventDefault();

const data = {

name: document.getElementById('name').value,

email: document.getElementById('email').value

};

await fetch('http://localhost:5000/submit', {

method: 'POST',

headers: {

'Content-Type': 'application/json'

},

body: JSON.stringify(data)

});

form.reset();

loadUsers();

});

async function loadUsers() {

const response = await fetch('http://localhost:5000/users');

const users = await response.json();

userList.innerHTML = '';

users.forEach(user => {

const li = document.createElement('li');

li.innerText = `${user.name} - ${user.email}`;

userList.appendChild(li);

});

}

loadUsers();