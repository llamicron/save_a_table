var app = new Vue({
  el: "#main",
  data: {
    activeTab: "",
    imagePath: "images/floor3.png"
  },
  methods: {
    setActiveTab(tabName) {
      this.activeTab = tabName;
      return true;
    }
  }
});
