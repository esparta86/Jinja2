var myModule=angular.module('mymodule',[]);
myModule.config(['$interpolateProvider', function($interpolateProvider) {
  $interpolateProvider.startSymbol('{[');
  $interpolateProvider.endSymbol(']}');
}]);

myModule.controller('testController', ['$scope', function($scope){
	$scope.init = function(){
      $scope.test ="test";
      $scope.xD = "xD";
      $scope.bind ="dddd";

	};
}]);