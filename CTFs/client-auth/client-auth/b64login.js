// add event listener to form submit
document.querySelector('form').addEventListener('submit', (event) => {
  event.preventDefault(); // prevent form from submitting

  const username = document.querySelector('#username').value;
  const password = document.querySelector('#password').value;

  // check if username and password are correct
  if (btoa(username) === 'WVdSdGFXNXBlZz09' && btoa(password) === 'cGFzc3dvcmQ=') {
    alert('Now you understand what btoa does?');
  } else {
    alert('Incorrect username or password.');
  }
});
