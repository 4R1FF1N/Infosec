// add event listener to form submit
document.querySelector('form').addEventListener('submit', (event) => {
  event.preventDefault(); // prevent form from submitting

  const username = document.querySelector('#username').value;
  const password = document.querySelector('#password').value;

  // check if username and password are correct
  if (username === 'admin321' && password === 'secretp@$$w0rd') {
    alert('Login successful!');
  } else {
    alert('Incorrect username or password.');
  }
});
