var app = angular.module("myApp", []);

app.controller('pageOneController', ['$scope', '$http', function ($scope, $http) {

     $scope.x="çalıştı";
     console.log($scope.x)
	 $scope.responseData;
var settings = {
     "url": "http://127.0.0.1:8080/api/tutorials",
     "method": "GET",
     "timeout": 0,
};
$http(settings).then(function (response) {
     console.log(response);
     $scope.responseData = response.data;
});
$scope.addshopcart=function(id){
	 var settings = {
     "url": "http://127.0.0.1:8080/api/tutorials/addshopcart/"+id,
     "method": "GET",
     "timeout": 0,
};
$http(settings).then(function (response) {
     console.log(response);	  
    
},
function(response){
	$scope.responseText =response.data.message
	 var x = document.getElementById("snackbar");
     x.className = "show";	 
     setTimeout(function(){ x.className = x.className.replace("show", ""); }, 5000);
}
);}


}]);

