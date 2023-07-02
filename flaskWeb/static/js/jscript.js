let i = 0
const input = document.forms["form"];
input[0].focus();

function changeFocus(event) {
  if(event.code == 'Backspace')
  {
    i--;
    input[i].focus();
    input[i].value = '';
  }
  else if(event.code == 'Enter')
  {
    i = 0;
    input[i].focus();
  }
  else{
    i++;
    input[i].focus();
  }
};

function delAllHistory() {
  jlist = document.getElementById('list');
  for (let listC = 0; listC < length.jlist; listC++) {
    jlist.remove();
  }
};

function delHistory() {
  jlist = document.getElementById('list');
  jlist.remove();
};