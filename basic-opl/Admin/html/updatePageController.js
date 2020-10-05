var app = angular.module("myApp", []);

app.controller('updatePageController', ['$scope', '$http', function ($scope, $http) {

$scope.url=  window.location.href;  
$scope.index=$scope.url.indexOf("id=");
$scope.id=$scope.url.slice($scope.index+3, $scope.url.length);
console.log($scope.id)
var settings = {
     "url": "http://127.0.0.1:8080/api/tutorials/"+$scope.id,
     "method": "GET",
     "timeout": 0,
};
$http(settings).then(function (response) {
     console.log(response);
     $scope.ProductDetailData = response.data;
});

$scope.update=function(){
	document.getElementById("loader").style.display = "block";
	var settings = {
     "url": "http://127.0.0.1:8080/api/tutorials/"+$scope.id,
     "method": "PUT",
     "timeout": 0,
	 "headers": {
    "Content-Type": "application/json"
  },
  "data": JSON.stringify({"name":$scope.ProductDetailData.name,"price":$scope.ProductDetailData.price,"amount":$scope.ProductDetailData.amount}),
};
$http(settings).then(function (response) {
     console.log(response);
	 document.getElementById("loader").style.display = "none";
     $scope.ProductDetailData = response.data;
	 $scope.responseText ="Your transaction has been completed successfully";
	 var x = document.getElementById("snackbar1");
     x.className = "show";	 
     setTimeout(function(){ x.className = x.className.replace("show", ""); }, 5000);
	 window.location.replace("ProductList.html");
},
function(response){
	document.getElementById("loader").style.display = "none";
	$scope.responseText ="An unexpected error has occurred. Data could not be updated!!";
	 var x = document.getElementById("snackbar");
     x.className = "show";	 
     setTimeout(function(){ x.className = x.className.replace("show", ""); }, 5000);
});
}

}]);
