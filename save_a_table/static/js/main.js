$('.carousel.carousel-slider').carousel({ fullWidth: true });

var app = new Vue({
  el: "#main",
  data: {
    activeTab: "floor3",
    onlyShowVacancy: true,
    tableData: {
      "floor3": [],
      "floor4": [],
      "floor5": [],
      "floor6": [],
    }
  },

  methods: {
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

    allTablesForFloor() {
      return this.tableData[this.activeTab];
    },

    tables() {
      if (this.onlyShowVacancy) {
        return this.vacantTables();
      } else {
        return this.allTablesForFloor();
      }
    },

    getTableData() {
      axios.get('/tableData')
        .then(response => {
          this.tableData = response.data;
        })
        .catch(function (error) {
          console.log(error);
        });
        return true;
    }
  },

  mounted: function() {
    updateTableInterval = window.setInterval(function() {
      app.getTableData();
    }, 2000)
  },

  watch: {
    activeTab: function() {
      this.updateImage();
    }
  }
});
