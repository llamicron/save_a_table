$('.carousel.carousel-slider').carousel({ fullWidth: true });

var app = new Vue({
  el: "#main",
  data: {
    activeTab: "floor3",
    onlyShowVacancy: true,

    tableData: {
      floor3: [
        { "name": "Table 1", "status": "Occupied" },
        { "name": "Table 2", "status": "Vacant" },
        { "name": "Table 3", "status": "Occupied" },
        { "name": "Table 4", "status": "Vacant" },
        { "name": "Table 5", "status": "Occupied" },
      ],
      floor4: [
        { "name": "Table 1", "status": "Vacant" },
        { "name": "Table 2", "status": "Vacant" },
        { "name": "Table 3", "status": "Occupied" },
        { "name": "Table 4", "status": "Occupied" },
        { "name": "Table 5", "status": "Vacant" },
      ],
      floor5: [
        { "name": "Table 1", "status": "Occupied" },
        { "name": "Table 2", "status": "Vacant" },
        { "name": "Table 3", "status": "Vacant" },
        { "name": "Table 4", "status": "Occupied" },
        { "name": "Table 5", "status": "Occupied" },
      ],
      floor6: [
        { "name": "Table 1", "status": "Vacant" },
        { "name": "Table 2", "status": "Occupied" },
        { "name": "Table 3", "status": "Occupied" },
        { "name": "Table 4", "status": "Vacant" },
        { "name": "Table 5", "status": "Occupied" },
      ]
    }
  },

  methods: {
    setActiveTab(tabName) {
      this.activeTab = tabName;
      this.updateImage();
      return true;
    },
    updateImage() {
      // Get the floor number and subtract 3 to make up for the index offset
      var index = this.activeTab.replace(/^\D+/g, '') - 3;
      $('.carousel').carousel('set', index);
    },
    vacantTables() {
      var vacantTables = [];
      this.tableData[this.activeTab].forEach(function(obj) {
        if (obj.status == 'Vacant') {
          vacantTables.push(obj);
        }
      }, this);
      return vacantTables;
    },

    allTables() {
      return this.tableData[this.activeTab];
    },

    tables() {
      if (this.onlyShowVacancy) {
        return this.vacantTables();
      } else {
        return this.allTables();
      }
    }
  }

  // mounted: function() {
  //   // Get data from Flask
  // }
});
