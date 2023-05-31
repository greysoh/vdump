const videoData = [];

for (videoRow of document.getElementsByTagName("ytd-rich-grid-row")) {
  for (video of videoRow.getElementsByTagName("ytd-rich-item-renderer")) {
    const ytImage = video.getElementsByTagName("yt-image")[0];
    const thumbUrl = ytImage.getElementsByTagName("img")[0].src;

    const ytString = video.getElementsByTagName("yt-formatted-string")[1];
    const titleAria = ytString.ariaLabel;
    const title = ytString.innerText;

    // Fix for nerds
    const url = ytImage.parentElement.href.split("&t")[0];

    videoData.push({
      title,
      titleAria,
      thumbUrl,
      url,

      description: null,
      isDownloaded: false
    })
  }
}

console.log(videoData);