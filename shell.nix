{
  pkgs ? import <nixpkgs> { },
}:
pkgs.mkShell {
  buildInputs = with pkgs; [
    SDL2
    libGL
  ];
  shellHook = ''
    export LD_LIBRARY_PATH="${
      pkgs.lib.makeLibraryPath [
        pkgs.SDL2
        pkgs.libGL
      ]
    }:$LD_LIBRARY_PATH"
  '';
}
