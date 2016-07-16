// Generated by CoffeeScript 1.3.3
var Worker, WorkerManager;

Worker = (function() {

  function Worker() {
    this.name = void 0;
    this.task = void 0;
    this.id = void 0;
    this.status = 'IDLE';
    this.skillset = void 0;
    this.create_time = '';
    return;
  }

  Worker.prototype.set_name = function(name) {
    return this.name = name;
  };

  Worker.prototype.get_name = function() {
    return this.name;
  };

  Worker.prototype.set_task = function(task) {
    return this.task = task;
  };

  Worker.prototype.get_task = function() {
    return this.task;
  };

  Worker.prototype.get_id = function() {
    return this.id;
  };

  Worker.prototype.set_status = function(status) {
    return this.status = status;
  };

  Worker.prototype.get_status = function() {
    return this.status;
  };

  Worker.prototype.set_skillset = function(skillset) {
    return this.skillset = skillset;
  };

  Worker.prototype.get_skillset = function() {
    return this.skillset;
  };

  return Worker;

})();

WorkerManager = (function() {
  var Internal, instance;

  function WorkerManager() {}

  instance = void 0;

  Internal = (function() {

    function Internal() {
      this.workers = new Array();
      return;
    }

    Internal.prototype.register = function() {};

    Internal.prototype.remove = function(uid) {};

    Internal.prototype.get_user_by_id = function(uid) {};

    Internal.prototype.get_user_by_name = function(name, start, num) {};

    Internal.prototype.get_user_by_task = function(task, start, num) {};

    Internal.prototype.get_users = function(task, start, num) {};

    Internal.prototype.update_user = function(uid, attr) {};

    return Internal;

  })();

  WorkerManager.get = function() {
    return instance != null ? instance : instance = new Internal();
  };

  return WorkerManager;

})();

module.exports = WorkerManager;
