# -*- coding: utf-8 -*-
# snapshottest: v1 - https://goo.gl/zC4yUc
from __future__ import unicode_literals

from snapshottest import Snapshot

snapshots = Snapshot()

snapshots[
    "test_index_view 1"
] = b'<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 3.2 Final//EN">\n<title>Redirecting...</title>\n<h1>Redirecting...</h1>\n<p>You should be redirected automatically to target URL: <a href="/login?next=%2F">/login?next=%2F</a>.  If not click the link.'

snapshots[
    "test_login_view 1"
] = b'<!doctype html>\n<html lang="en">\n  <head>\n    <!-- Required meta tags -->\n    <meta charset="utf-8">\n    <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">\n\n    <!-- Bootstrap CSS -->\n    <link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.5.2/css/bootstrap.min.css" integrity="sha384-JcKb8q3iqJ61gNV9KGb8thSsNjpSL0n8PARn9HuZOnIxN0hoP+VmmDGMN5t9UJ0Z" crossorigin="anonymous">\n\n    \n    <title>Sign In - Flask Blog</title>\n    \n\n  </head>\n  <body>\n    <div>\n      Flask Blog:\n      <a href="/index">Home</a>\n      \n      <a href="/login">Login</a>\n      \n    </div>\n    <hr>\n    \n    \n    \n    \n    <h1>Sign In</h1>\n    <form action="" method="post" novalidate>\n        <input id="csrf_token" name="csrf_token" type="hidden" value="ImU5MGJmMTJhZjVmNGI1ODczNzc2ODQ0MGIyODU1MzAxMTVmOWMyNmEi.X2iyHA.c6_rFNW2zqFKl8H_gqGDTivy4EU">\n        <p>\n            <label for="username">Username</label><br>\n            <input id="username" name="username" required size="32" type="text" value=""><br>\n            \n        </p>\n        <p>\n            <label for="password">Password</label><br>\n            <input id="password" name="password" required size="32" type="password" value=""><br>\n            \n        </p>\n        <p><input id="remember_me" name="remember_me" type="checkbox" value="y"> <label for="remember_me">Remember Me</label></p>\n        <p><input id="submit" name="submit" type="submit" value="Sign In"></p>\n        <p>New User? <a href="/register">Click to Register!</a></p>\n    </form>\n\n\n    <!-- Optional JavaScript -->\n    <!-- jQuery first, then Popper.js, then Bootstrap JS -->\n    <script src="https://code.jquery.com/jquery-3.5.1.slim.min.js" integrity="sha384-DfXdz2htPH0lsSSs5nCTpuj/zy4C+OGpamoFVy38MVBnE+IbbVYUew+OrCXaRkfj" crossorigin="anonymous"></script>\n    <script src="https://cdn.jsdelivr.net/npm/popper.js@1.16.1/dist/umd/popper.min.js" integrity="sha384-9/reFTGAW83EW2RDu2S0VKaIzap3H66lZH81PoYlFhbGU+6BZp6G7niu735Sk7lN" crossorigin="anonymous"></script>\n    <script src="https://stackpath.bootstrapcdn.com/bootstrap/4.5.2/js/bootstrap.min.js" integrity="sha384-B4gt1jrGC7Jh4AgTPSdUtOBvfO8shuf57BaghqFfPlYxofvL8/KUEfYiJOMMV+rV" crossorigin="anonymous"></script>\n  </body>\n</html>'
