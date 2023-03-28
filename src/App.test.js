const fs = require('fs');

describe('App.js', () => {
  it('should update the file contents', () => {
    const filePath = './src/App.js';
    const newContent = 'const message = "Hello, World!";';
    fs.writeFileSync(filePath, newContent);
    const updatedContent = fs.readFileSync(filePath, 'utf-8');
    expect(updatedContent).toEqual(newContent);
  });
});
