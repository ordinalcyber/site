function showLevel(level) {
  const levels = ['debutant', 'intermediaire', 'expert'];
  levels.forEach(id => {
    document.getElementById(id).classList.remove('active');
  });
  document.getElementById(level).classList.add('active');
}
