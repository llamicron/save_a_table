$('.carousel.carousel-slider').carousel({ fullWidth: true });

var app = new Vue({
  el: "#main",
  data: {
    activeTab: "",
    imagePath: "images/floor3.png"
  },
  methods: {
    setActiveTab(tabName) {
      this.activeTab = tabName;
      this.updateImage(tabName);
      return true;
    },
    updateImage(selectedTab) {
      // Get the floor number and subtract 3 to make up for the index offset
      var index = selectedTab.replace(/^\D+/g, '') - 3;
      $('.carousel').carousel('set', index);
    },

  }
});
