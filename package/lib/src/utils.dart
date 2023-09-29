import 'dart:io';

import 'package:flutter/material.dart';
import 'package:flutter/widgets.dart';
import 'package:window_manager/window_manager.dart';

import 'utils/desktop.dart';

class WindowCloseListener extends WindowListener {
  final Function? onClose;

  WindowCloseListener(this.onClose);

  @override
  void onWindowClose() {
    onClose?.call();
  }
}

Future setupDesktop({Function? onClose}) async {
  if (isDesktop()) {
    WidgetsFlutterBinding.ensureInitialized();
    await windowManager.ensureInitialized();

    if (onClose != null) {
      windowManager.addListener(WindowCloseListener(onClose));
    }

    Map<String, String> env = Platform.environment;
    var hideWindowOnStart = env["FLET_HIDE_WINDOW_ON_START"];
    debugPrint("hideWindowOnStart: $hideWindowOnStart");

    await windowManager.waitUntilReadyToShow(null, () async {
      if (hideWindowOnStart == null) {
        await windowManager.show();
        await windowManager.focus();
      }
    });
  }
}
