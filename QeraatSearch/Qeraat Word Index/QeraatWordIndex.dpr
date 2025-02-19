program QeraatWordIndex;

uses
  Vcl.Forms,
  Master in 'Master.pas' {MasterF};

{$R *.res}

begin
  Application.Initialize;
  Application.MainFormOnTaskbar := True;
  Application.CreateForm(TMasterF, MasterF);
  Application.Run;
end.
