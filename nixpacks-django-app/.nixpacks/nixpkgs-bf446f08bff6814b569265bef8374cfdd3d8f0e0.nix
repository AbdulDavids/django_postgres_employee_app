{ }:

let pkgs = import (fetchTarball "https://github.com/NixOS/nixpkgs/archive/bf446f08bff6814b569265bef8374cfdd3d8f0e0.tar.gz") { overlays = [  ]; };
in with pkgs;
  let
    APPEND_LIBRARY_PATH = "${lib.makeLibraryPath [ stdenv.cc.cc.lib zlib ] }";
    myLibraries = writeText "libraries" ''
      export LD_LIBRARY_PATH="${APPEND_LIBRARY_PATH}:$LD_LIBRARY_PATH"
      
    '';
  in
    buildEnv {
      name = "bf446f08bff6814b569265bef8374cfdd3d8f0e0-env";
      paths = [
        (runCommand "bf446f08bff6814b569265bef8374cfdd3d8f0e0-env" { } ''
          mkdir -p $out/etc/profile.d
          cp ${myLibraries} $out/etc/profile.d/bf446f08bff6814b569265bef8374cfdd3d8f0e0-env.sh
        '')
        gcc postgresql python3
      ];
    }
