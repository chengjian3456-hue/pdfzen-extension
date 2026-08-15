// PDFzen extension popup — open the matching tool page in a new tab.
// No permissions, no network calls: the launcher simply deep-links to the
// live, client-side tool. Files are processed in the browser, never uploaded.
document.querySelectorAll('[data-href]').forEach(function (btn) {
  btn.addEventListener('click', function () {
    chrome.tabs.create({ url: btn.dataset.href });
  });
});
