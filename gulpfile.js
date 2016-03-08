var gulp       = require('gulp');
var less       = require('gulp-less');
var path       = require('path');
var minify_css = require('gulp-minify-css');
var gutil      = require('gulp-util');
var sourcemaps = require('gulp-sourcemaps');

var assets_path = './assets',
  less_path = assets_path + '/less';

gulp.task('less', function () {
  return gulp.src(less_path + '/*.less')
    .pipe(sourcemaps.init())
    .pipe(less({
      paths: [path.join(less_path, '/modules/')],
      compress: true
    }).on('error', gutil.log))
    .pipe(minify_css({
      keepBreaks: false
    }))
    .pipe(sourcemaps.write())
    .pipe(gulp.dest('./static'));
});

gulp.task('default', function() {
  gulp.watch(less_path + '/**/*.less', function(event) {
    gulp.start('less');
  });
});

