angular.module("report").controller("reportCtrl", function ($scope, $http) {

  $scope.app = "List of Reports";
  $scope.reports = [];
  $scope.users = [];

  var getUsers = function () {
    $http.get("http://127.0.0.1:8000/users/").success(function (data) {
      $scope.users = data;
      console.log(data)
    }).error(function (data, status) {
  
    });
  };

  var getReports = function () {
    $http.get("http://127.0.0.1:8000/reports/").success(function (data) {
      $scope.reports = data;
      console.log(data)
    }).error(function (data, status) {
      
    });
  };

  $scope.openModal = function(report) {   
    $scope.modalData = report;
  };

  getUsers()
  getReports()

});