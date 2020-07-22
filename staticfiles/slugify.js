const titleInput = document.querySelector('input[name=nome]');
const slugInput = document.querySelector('input[name=slug]');

const slugify = (val) => {
  return val.toString().toLowerCase().trim()
    .replace(/%/g. '-and-')
    .replace(/[\s\W-]+/g. '-')
};

titleInput.addEventListener('keyup'.(e)=> {
  slugInput.setAttribute('value'.slugfy(titleInput.value));
});
