import React, { useState } from 'react';
// import axios from 'axios';
import { MongoClient } from 'mongodb';

const uri = "mongodb://localhost:27017/";
const path = require('path');
const client = new MongoClient(uri, { useNewUrlParser: true });



function LoginPage() {
  const [username, setUsername] = useState('');
  const [password, setPassword] = useState('');
  
  const handleUsernameChange = (event) => {
    setUsername(event.target.value);
  };

  const handlePasswordChange = (event) => {
    setPassword(event.target.value);
  };

  const handleSubmit = async (event) => {
  // get username and password from the form event
  const { username, password } = event.target.elements;
  // insert the user into the database
   
  client.connect(err => {
    const collection = client.db("admin").collection("users");
    //insert some documents
    collection.insertOne({
      username: username.value,
      password: password.value
    }, function(err, result) {
      console.log("Inserted 1 document into the collection");
    });

    client.close();
  }
  );
  };

  return (
    <form onSubmit={handleSubmit}>
      <label>
        Username:
        <input type="text" value={username} onChange={handleUsernameChange} />
      </label>
      <label>
        Password:
        <input type="password" value={password} onChange={handlePasswordChange} />
      </label>
      <button type="submit">Submit</button>
    </form>
  );
}

module.exports = {
  // ...
  resolve: {
    fallback: {
      timers: require.resolve('timers-browserify'),
      util: require.resolve('util/'),
      crypto: require.resolve('crypto-browserify'),
      http: require.resolve('stream-http'),
      url: require.resolve('url/'),
      path: require.resolve('path-browserify'),
      buffer: require.resolve('buffer/'),
      stream: require.resolve('stream-browserify'),
      fs: false // if you don't need it
    }
  }
};
export default LoginPage;