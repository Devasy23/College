let submissionsData = new Map(); // store the submissions data in a map

// fetch all submissions for the user and store them in the map
async function FetchData(userId) {
  const submissions = await fetch(`https://codeforces.com/api/user.status?handle=${userId}`)
    .then(response => response.json())
    .then(data => data.result);
  
  const submissionDataMap = new Map();
  
  submissions.forEach(submission => {
    const dateStr = new Date(submission.creationTimeSeconds * 1000).toLocaleDateString();
    const problemResult = submission.verdict;
    
    if (!submissionDataMap.has(dateStr)) {
      submissionDataMap.set(dateStr, { totalSubmissions: 1, acceptedSubmissions: 0 });
    } else {
      submissionDataMap.get(dateStr).totalSubmissions += 1;
    }
    
    if (problemResult === "OK") {
      submissionDataMap.get(dateStr).acceptedSubmissions += 1;
    }
  });
  
  return submissionDataMap;
}


// console.log(fetchData("Bakasta07"));


function updateTodayCount(data) {
  const today = new Date().toLocaleDateString();
  const todayCount = data.has(today) ? data.get(today).totalSubmissions : 0;
  const spanElement = document.getElementById("todaycount");
  spanElement.textContent = todayCount;
  if (todayCount >= 7) {
    spanElement.style.color = "green";
  } else if (todayCount >= 3) {
    spanElement.style.color = "yellow";
  } else {
    spanElement.style.color = "red";
  }
}





async function getData() {
  const data = [];
  const fetchData = await FetchData("tourist");
  for (let i = 6; i >= 0; i--) {
    const date = new Date();
    date.setDate(date.getDate() - i);
    const dateStr = date.toLocaleDateString();
    const totalSubmissions = fetchData.has(dateStr) ? fetchData.get(dateStr).totalSubmissions : 0;
    const acceptedSubmissions = fetchData.has(dateStr) ? fetchData.get(dateStr).acceptedSubmissions : 0;
    data.push({ date: dateStr, totalSubmissions, acceptedSubmissions });
  }
  return data;
}


async function displayChart() {
  const data = await getData();
  // console.log(data);
  const labels = data.map(obj => obj.date);
  const totalSubmissionsData = data.map(obj => obj.totalSubmissions);
  const acceptedSubmissionsData = data.map(obj => obj.acceptedSubmissions);
  updateTodayCount(submissionsData);
  const ctx = document.getElementById("myChart").getContext("2d");
  const chart = new Chart(ctx, {
    type: "bar",
    data: {
      labels: labels,
      datasets: [
        {
          label: "Total Submissions",
          data: totalSubmissionsData,
          backgroundColor: "rgba(54, 162, 235, 0.5)",
          borderColor: "rgba(54, 162, 235, 1)",
          borderWidth: 1
        },
        {
          label: "Accepted Submissions",
          data: acceptedSubmissionsData,
          backgroundColor: "rgba(255, 99, 132, 0.5)",
          borderColor: "rgba(255, 99, 132, 1)",
          borderWidth: 1
        }
      ]
    },
    options: {
      scales: {
        yAxes: [
          {
            ticks: {
              beginAtZero: true
            }
          }
        ]
      }
    }
  });
}

displayChart();
