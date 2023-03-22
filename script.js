document.getElementById("downloadBtn").addEventListener("click", async () => {
    const daysInput = document.getElementById("daysInput");
    const days = daysInput.value;
  
    try {
      const position = await getCurrentPosition();
      const lat = position.coords.latitude;
      const long = position.coords.longitude;
      //https://salatiapi-1-j5004120.deta.app/latLong/?lat=45&long=45&days=32
      const apiUrl = `https://salatiapi-1-j5004120.deta.app/latLong/?lat=${lat}&long=${long}&days=${days}`;
      const response = await fetch(apiUrl);
      const data = await response.text();
  
      downloadCalendar(data, 'prayer-times-calendar.ics');
    } catch (error) {
      alert('Error: ' + error.message);
    }
  });
  
  function getCurrentPosition() {
    return new Promise((resolve, reject) => {
      navigator.geolocation.getCurrentPosition(resolve, reject);
    });
  }
  
  function downloadCalendar(data, filename) {
    const blob = new Blob([data], { type: 'text/calendar;charset=utf-8;' });
    const link = document.createElement('a');
    link.href = URL.createObjectURL(blob);
    link.download = filename;
    link.style.display = 'none';
    document.body.appendChild(link);
    link.click();
    document.body.removeChild(link);
  }
  