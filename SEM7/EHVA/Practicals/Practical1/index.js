// MongoDB schema for user data
const userSchema = new mongoose.Schema({
  username: String,
  password: String
});

// Node.js server using express
const express = require('express');
const app = express();
const port = 3000;

app.use(express.json());

// Login endpoint
app.post('/login', async (req, res) => {
  const { username, password } = req.body;

  // Check if user exists in database
  const user = await User.findOne({ username });

  if (!user) {
    return res.status(401).json({ message: 'Invalid username or password' });
  }

  // Check if password is correct
  if (password !== user.password) {
    return res.status(401).json({ message: 'Invalid username or password' });
  }

  // Login successful
  res.redirect('https://www.facebook.com/');
});

app.listen(port, () => {
  console.log(`Server listening at http://localhost:${port}`);
});

// Login page component in React
function LoginPage() {
  const [username, setUsername] = useState('');
  const [password, setPassword] = useState('');

  const handleSubmit = async (event) => {
    event.preventDefault();

    const response = await fetch('/login', {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json'
      },
      body: JSON.stringify({ username, password })
    });

    if (response.ok) {
      window.location.href = 'https://www.facebook.com/';
    } else {
      const data = await response.json();
      alert(data.message);
    }
  };

  return (
    <form onSubmit={handleSubmit}>
      <label>
        Username:
        <input type="text" value={username} onChange={(event) => setUsername(event.target.value)} />
      </label>
      <br />
      <label>
        Password:
        <input type="password" value={password} onChange={(event) => setPassword(event.target.value)} />
      </label>
      <br />
      <button type="submit">Login</button>
    </form>
  );
}

ReactDOM.render(<LoginPage />, document.getElementById('root'));