/**
 * Listen for clicks on the buttons
 */
function listenForClicks() {
  document.addEventListener("click", (e) => {

    console.log('MDL X')
    // get the tabs
    browser.tabs.query({ active: true, currentWindow: true })
      .then(function (tabs) {
        // assume that there is only one active. check wether it is github.
        match = tabs[0].url.match(/https:\/\/github.com\/(\w*)\/(\w*)/)
        if (match) {
          var owner = match[1]
          var repo = match[2]

          document.querySelector("#content-status").textContent = `Querying for ${owner}/${repo}` 
          
          fetch("https://openwhisk.eu-gb.bluemix.net/api/v1/web/luebken_dev/default/mainAction.json?reference_repo=" + owner + "/" + repo)
            .then(function (response) {
              return response.json();
            })
            .then(function (json) {
              document.querySelector("#content-status").textContent = `Done` 
              document.querySelector("#content-result").textContent = json.similar_repos              
              console.log('json', json)
            })
            .catch(function (y) {
              console.log('fetched error', y)
            });
        }

      })


    /**
     * Just log the error to the console.
     */
    function reportError(error) {
      console.error(`Could not beastify: ${error}`);
    }
  });
}

/**
 * There was an error executing the script.
 * Display the popup's error message, and hide the normal UI.
 */
function reportExecuteScriptError(error) {
  document.querySelector("#popup-content").classList.add("hidden");
  document.querySelector("#error-content").classList.remove("hidden");
  console.error(`Failed to execute beastify content script: ${error.message}`);
}

/**
 * When the popup loads, inject a content script into the active tab,
 * and add a click handler.
 * If we couldn't inject the script, handle the error.
 */
browser.tabs.executeScript({ file: "/content_scripts/beastify.js" })
  .then(listenForClicks)
  .catch(reportExecuteScriptError);
