var app = angular.module("myApp", []);

app.controller('SecondPageController', ['$scope', '$http', function ($scope, $http) {

     $scope.x="çalıştı";
     console.log($scope.x)
	 $scope.ProductData;
var settings = {
     "url": "http://127.0.0.1:8080/api/tutorials",
     "method": "GET",
     "timeout": 0,
};
$http(settings).then(function (response) {
     console.log(response);
     $scope.ProductData = response.data;
});



}]);