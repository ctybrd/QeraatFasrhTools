
{***********************************************}
{                                               }
{               XML Data Binding                }
{                                               }
{         Generated on: 04/08/2018 09:39:02 ã   }
{       Generated from: H:\temp\J.xml           }
{   Settings stored in: H:\temp\J.xdb           }
{                                               }
{***********************************************}

unit J;

interface

uses xmldom, XMLDoc, XMLIntf;

type

{ Forward Decls }

  IXMLXfdfType = interface;
  IXMLAnnotsType = interface;
  IXMLStampType = interface;
  IXMLStampTypeList = interface;
  IXMLPopupType = interface;
  IXMLLineType = interface;
  IXMLLineTypeList = interface;
  IXMLFType = interface;
  IXMLIdsType = interface;

{ IXMLXfdfType }

  IXMLXfdfType = interface(IXMLNode)
    ['{F65FA3EE-0416-4851-B1F1-17B1BDA2A5D3}']
    { Property Accessors }
    function Get_Xmlns: UnicodeString;
    function Get_Annots: IXMLAnnotsType;
    function Get_F: IXMLFType;
    function Get_Ids: IXMLIdsType;
    procedure Set_Xmlns(Value: UnicodeString);
    { Methods & Properties }
    property Xmlns: UnicodeString read Get_Xmlns write Set_Xmlns;
    property Annots: IXMLAnnotsType read Get_Annots;
    property F: IXMLFType read Get_F;
    property Ids: IXMLIdsType read Get_Ids;
  end;

{ IXMLAnnotsType }

  IXMLAnnotsType = interface(IXMLNode)
    ['{E140F037-E96F-4B3F-95ED-73EE6AD61FCA}']
    { Property Accessors }
    function Get_Stamp: IXMLStampTypeList;
    function Get_Line: IXMLLineTypeList;
    { Methods & Properties }
    property Stamp: IXMLStampTypeList read Get_Stamp;
    property Line: IXMLLineTypeList read Get_Line;
  end;

{ IXMLStampType }

  IXMLStampType = interface(IXMLNode)
    ['{7299464C-AD12-45F6-8253-7F0A54FF4B62}']
    { Property Accessors }
    function Get_Color: Integer;
    function Get_Creationdate: Integer;
    function Get_Flags: Integer;
    function Get_Date: Integer;
    function Get_Name: Integer;
    function Get_Icon: Integer;
    function Get_Page: Integer;
    function Get_Rect: UnicodeString;
    function Get_Subject: Integer;
    function Get_Title: Integer;
    function Get_Appearance: Integer;
    function Get_Popup: IXMLPopupType;
    procedure Set_Color(Value: Integer);
    procedure Set_Creationdate(Value: Integer);
    procedure Set_Flags(Value: Integer);
    procedure Set_Date(Value: Integer);
    procedure Set_Name(Value: Integer);
    procedure Set_Icon(Value: Integer);
    procedure Set_Page(Value: Integer);
    procedure Set_Rect(Value: UnicodeString);
    procedure Set_Subject(Value: Integer);
    procedure Set_Title(Value: Integer);
    procedure Set_Appearance(Value: Integer);
    { Methods & Properties }
    property Color: Integer read Get_Color write Set_Color;
    property Creationdate: Integer read Get_Creationdate write Set_Creationdate;
    property Flags: Integer read Get_Flags write Set_Flags;
    property Date: Integer read Get_Date write Set_Date;
    property Name: Integer read Get_Name write Set_Name;
    property Icon: Integer read Get_Icon write Set_Icon;
    property Page: Integer read Get_Page write Set_Page;
    property Rect: UnicodeString read Get_Rect write Set_Rect;
    property Subject: Integer read Get_Subject write Set_Subject;
    property Title: Integer read Get_Title write Set_Title;
    property Appearance: Integer read Get_Appearance write Set_Appearance;
    property Popup: IXMLPopupType read Get_Popup;
  end;

{ IXMLStampTypeList }

  IXMLStampTypeList = interface(IXMLNodeCollection)
    ['{DA7BAE9A-911F-45A5-B926-D9ABA4A81D93}']
    { Methods & Properties }
    function Add: IXMLStampType;
    function Insert(const Index: Integer): IXMLStampType;

    function Get_Item(Index: Integer): IXMLStampType;
    property Items[Index: Integer]: IXMLStampType read Get_Item; default;
  end;

{ IXMLPopupType }

  IXMLPopupType = interface(IXMLNode)
    ['{F9B5D6A9-A90D-4B2B-A735-27D3AB2AE34B}']
    { Property Accessors }
    function Get_Flags: Integer;
    function Get_Open: Integer;
    function Get_Page: Integer;
    function Get_Rect: UnicodeString;
    procedure Set_Flags(Value: Integer);
    procedure Set_Open(Value: Integer);
    procedure Set_Page(Value: Integer);
    procedure Set_Rect(Value: UnicodeString);
    { Methods & Properties }
    property Flags: Integer read Get_Flags write Set_Flags;
    property Open: Integer read Get_Open write Set_Open;
    property Page: Integer read Get_Page write Set_Page;
    property Rect: UnicodeString read Get_Rect write Set_Rect;
  end;

{ IXMLLineType }

  IXMLLineType = interface(IXMLNode)
    ['{D2F29527-C0A7-4CCF-9047-6D73720F4A2D}']
    { Property Accessors }
    function Get_Color: Integer;
    function Get_Creationdate: Integer;
    function Get_Flags: Integer;
    function Get_Start: UnicodeString;
    function Get_End_: UnicodeString;
    function Get_Date: Integer;
    function Get_Name: Integer;
    function Get_Page: Integer;
    function Get_Rect: UnicodeString;
    function Get_Subject: Integer;
    function Get_Title: Integer;
    function Get_Width: UnicodeString;
    function Get_Style: Integer;
    function Get_Interiorcolor: Integer;
    function Get_Popup: IXMLPopupType;
    procedure Set_Color(Value: Integer);
    procedure Set_Creationdate(Value: Integer);
    procedure Set_Flags(Value: Integer);
    procedure Set_Start(Value: UnicodeString);
    procedure Set_End_(Value: UnicodeString);
    procedure Set_Date(Value: Integer);
    procedure Set_Name(Value: Integer);
    procedure Set_Page(Value: Integer);
    procedure Set_Rect(Value: UnicodeString);
    procedure Set_Subject(Value: Integer);
    procedure Set_Title(Value: Integer);
    procedure Set_Width(Value: UnicodeString);
    procedure Set_Style(Value: Integer);
    procedure Set_Interiorcolor(Value: Integer);
    { Methods & Properties }
    property Color: Integer read Get_Color write Set_Color;
    property Creationdate: Integer read Get_Creationdate write Set_Creationdate;
    property Flags: Integer read Get_Flags write Set_Flags;
    property Start: UnicodeString read Get_Start write Set_Start;
    property End_: UnicodeString read Get_End_ write Set_End_;
    property Date: Integer read Get_Date write Set_Date;
    property Name: Integer read Get_Name write Set_Name;
    property Page: Integer read Get_Page write Set_Page;
    property Rect: UnicodeString read Get_Rect write Set_Rect;
    property Subject: Integer read Get_Subject write Set_Subject;
    property Title: Integer read Get_Title write Set_Title;
    property Width: UnicodeString read Get_Width write Set_Width;
    property Style: Integer read Get_Style write Set_Style;
    property Interiorcolor: Integer read Get_Interiorcolor write Set_Interiorcolor;
    property Popup: IXMLPopupType read Get_Popup;
  end;

{ IXMLLineTypeList }

  IXMLLineTypeList = interface(IXMLNodeCollection)
    ['{FCBBF810-EBB8-4F02-BDCC-BE698EE2BD24}']
    { Methods & Properties }
    function Add: IXMLLineType;
    function Insert(const Index: Integer): IXMLLineType;

    function Get_Item(Index: Integer): IXMLLineType;
    property Items[Index: Integer]: IXMLLineType read Get_Item; default;
  end;

{ IXMLFType }

  IXMLFType = interface(IXMLNode)
    ['{78919162-01D7-4649-A52C-5FACD345649E}']
    { Property Accessors }
    function Get_Href: UnicodeString;
    procedure Set_Href(Value: UnicodeString);
    { Methods & Properties }
    property Href: UnicodeString read Get_Href write Set_Href;
  end;

{ IXMLIdsType }

  IXMLIdsType = interface(IXMLNode)
    ['{81429D2A-4C15-45C9-95B8-54CCAE427C11}']
    { Property Accessors }
    function Get_Original: Integer;
    function Get_Modified: Integer;
    procedure Set_Original(Value: Integer);
    procedure Set_Modified(Value: Integer);
    { Methods & Properties }
    property Original: Integer read Get_Original write Set_Original;
    property Modified: Integer read Get_Modified write Set_Modified;
  end;

{ Forward Decls }

  TXMLXfdfType = class;
  TXMLAnnotsType = class;
  TXMLStampType = class;
  TXMLStampTypeList = class;
  TXMLPopupType = class;
  TXMLLineType = class;
  TXMLLineTypeList = class;
  TXMLFType = class;
  TXMLIdsType = class;

{ TXMLXfdfType }

  TXMLXfdfType = class(TXMLNode, IXMLXfdfType)
  protected
    { IXMLXfdfType }
    function Get_Xmlns: UnicodeString;
    function Get_Annots: IXMLAnnotsType;
    function Get_F: IXMLFType;
    function Get_Ids: IXMLIdsType;
    procedure Set_Xmlns(Value: UnicodeString);
  public
    procedure AfterConstruction; override;
  end;

{ TXMLAnnotsType }

  TXMLAnnotsType = class(TXMLNode, IXMLAnnotsType)
  private
    FStamp: IXMLStampTypeList;
    FLine: IXMLLineTypeList;
  protected
    { IXMLAnnotsType }
    function Get_Stamp: IXMLStampTypeList;
    function Get_Line: IXMLLineTypeList;
  public
    procedure AfterConstruction; override;
  end;

{ TXMLStampType }

  TXMLStampType = class(TXMLNode, IXMLStampType)
  protected
    { IXMLStampType }
    function Get_Color: Integer;
    function Get_Creationdate: Integer;
    function Get_Flags: Integer;
    function Get_Date: Integer;
    function Get_Name: Integer;
    function Get_Icon: Integer;
    function Get_Page: Integer;
    function Get_Rect: UnicodeString;
    function Get_Subject: Integer;
    function Get_Title: Integer;
    function Get_Appearance: Integer;
    function Get_Popup: IXMLPopupType;
    procedure Set_Color(Value: Integer);
    procedure Set_Creationdate(Value: Integer);
    procedure Set_Flags(Value: Integer);
    procedure Set_Date(Value: Integer);
    procedure Set_Name(Value: Integer);
    procedure Set_Icon(Value: Integer);
    procedure Set_Page(Value: Integer);
    procedure Set_Rect(Value: UnicodeString);
    procedure Set_Subject(Value: Integer);
    procedure Set_Title(Value: Integer);
    procedure Set_Appearance(Value: Integer);
  public
    procedure AfterConstruction; override;
  end;

{ TXMLStampTypeList }

  TXMLStampTypeList = class(TXMLNodeCollection, IXMLStampTypeList)
  protected
    { IXMLStampTypeList }
    function Add: IXMLStampType;
    function Insert(const Index: Integer): IXMLStampType;

    function Get_Item(Index: Integer): IXMLStampType;
  end;

{ TXMLPopupType }

  TXMLPopupType = class(TXMLNode, IXMLPopupType)
  protected
    { IXMLPopupType }
    function Get_Flags: Integer;
    function Get_Open: Integer;
    function Get_Page: Integer;
    function Get_Rect: UnicodeString;
    procedure Set_Flags(Value: Integer);
    procedure Set_Open(Value: Integer);
    procedure Set_Page(Value: Integer);
    procedure Set_Rect(Value: UnicodeString);
  end;

{ TXMLLineType }

  TXMLLineType = class(TXMLNode, IXMLLineType)
  protected
    { IXMLLineType }
    function Get_Color: Integer;
    function Get_Creationdate: Integer;
    function Get_Flags: Integer;
    function Get_Start: UnicodeString;
    function Get_End_: UnicodeString;
    function Get_Date: Integer;
    function Get_Name: Integer;
    function Get_Page: Integer;
    function Get_Rect: UnicodeString;
    function Get_Subject: Integer;
    function Get_Title: Integer;
    function Get_Width: UnicodeString;
    function Get_Style: Integer;
    function Get_Interiorcolor: Integer;
    function Get_Popup: IXMLPopupType;
    procedure Set_Color(Value: Integer);
    procedure Set_Creationdate(Value: Integer);
    procedure Set_Flags(Value: Integer);
    procedure Set_Start(Value: UnicodeString);
    procedure Set_End_(Value: UnicodeString);
    procedure Set_Date(Value: Integer);
    procedure Set_Name(Value: Integer);
    procedure Set_Page(Value: Integer);
    procedure Set_Rect(Value: UnicodeString);
    procedure Set_Subject(Value: Integer);
    procedure Set_Title(Value: Integer);
    procedure Set_Width(Value: UnicodeString);
    procedure Set_Style(Value: Integer);
    procedure Set_Interiorcolor(Value: Integer);
  public
    procedure AfterConstruction; override;
  end;

{ TXMLLineTypeList }

  TXMLLineTypeList = class(TXMLNodeCollection, IXMLLineTypeList)
  protected
    { IXMLLineTypeList }
    function Add: IXMLLineType;
    function Insert(const Index: Integer): IXMLLineType;

    function Get_Item(Index: Integer): IXMLLineType;
  end;

{ TXMLFType }

  TXMLFType = class(TXMLNode, IXMLFType)
  protected
    { IXMLFType }
    function Get_Href: UnicodeString;
    procedure Set_Href(Value: UnicodeString);
  end;

{ TXMLIdsType }

  TXMLIdsType = class(TXMLNode, IXMLIdsType)
  protected
    { IXMLIdsType }
    function Get_Original: Integer;
    function Get_Modified: Integer;
    procedure Set_Original(Value: Integer);
    procedure Set_Modified(Value: Integer);
  end;

{ Global Functions }

function Getxfdf(Doc: IXMLDocument): IXMLXfdfType;
function Loadxfdf(const FileName: string): IXMLXfdfType;
function Newxfdf: IXMLXfdfType;

const
  TargetNamespace = 'http://ns.adobe.com/xfdf/';

implementation

{ Global Functions }

function Getxfdf(Doc: IXMLDocument): IXMLXfdfType;
begin
  Result := Doc.GetDocBinding('xfdf', TXMLXfdfType, TargetNamespace) as IXMLXfdfType;
end;

function Loadxfdf(const FileName: string): IXMLXfdfType;
begin
  Result := LoadXMLDocument(FileName).GetDocBinding('xfdf', TXMLXfdfType, TargetNamespace) as IXMLXfdfType;
end;

function Newxfdf: IXMLXfdfType;
begin
  Result := NewXMLDocument.GetDocBinding('xfdf', TXMLXfdfType, TargetNamespace) as IXMLXfdfType;
end;

{ TXMLXfdfType }

procedure TXMLXfdfType.AfterConstruction;
begin
  RegisterChildNode('annots', TXMLAnnotsType);
  RegisterChildNode('f', TXMLFType);
  RegisterChildNode('ids', TXMLIdsType);
  inherited;
end;

function TXMLXfdfType.Get_Xmlns: UnicodeString;
begin
  Result := AttributeNodes['xmlns'].Text;
end;

procedure TXMLXfdfType.Set_Xmlns(Value: UnicodeString);
begin
  SetAttribute('xmlns', Value);
end;

function TXMLXfdfType.Get_Annots: IXMLAnnotsType;
begin
  Result := ChildNodes['annots'] as IXMLAnnotsType;
end;

function TXMLXfdfType.Get_F: IXMLFType;
begin
  Result := ChildNodes[WideString('f')] as IXMLFType;
end;

function TXMLXfdfType.Get_Ids: IXMLIdsType;
begin
  Result := ChildNodes['ids'] as IXMLIdsType;
end;

{ TXMLAnnotsType }

procedure TXMLAnnotsType.AfterConstruction;
begin
  RegisterChildNode('stamp', TXMLStampType);
  RegisterChildNode('line', TXMLLineType);
  FStamp := CreateCollection(TXMLStampTypeList, IXMLStampType, 'stamp') as IXMLStampTypeList;
  FLine := CreateCollection(TXMLLineTypeList, IXMLLineType, 'line') as IXMLLineTypeList;
  inherited;
end;

function TXMLAnnotsType.Get_Stamp: IXMLStampTypeList;
begin
  Result := FStamp;
end;

function TXMLAnnotsType.Get_Line: IXMLLineTypeList;
begin
  Result := FLine;
end;

{ TXMLStampType }

procedure TXMLStampType.AfterConstruction;
begin
  RegisterChildNode('popup', TXMLPopupType);
  inherited;
end;

function TXMLStampType.Get_Color: Integer;
begin
  Result := AttributeNodes['color'].NodeValue;
end;

procedure TXMLStampType.Set_Color(Value: Integer);
begin
  SetAttribute('color', Value);
end;

function TXMLStampType.Get_Creationdate: Integer;
begin
  Result := AttributeNodes['creationdate'].NodeValue;
end;

procedure TXMLStampType.Set_Creationdate(Value: Integer);
begin
  SetAttribute('creationdate', Value);
end;

function TXMLStampType.Get_Flags: Integer;
begin
  Result := AttributeNodes['flags'].NodeValue;
end;

procedure TXMLStampType.Set_Flags(Value: Integer);
begin
  SetAttribute('flags', Value);
end;

function TXMLStampType.Get_Date: Integer;
begin
  Result := AttributeNodes['date'].NodeValue;
end;

procedure TXMLStampType.Set_Date(Value: Integer);
begin
  SetAttribute('date', Value);
end;

function TXMLStampType.Get_Name: Integer;
begin
  Result := AttributeNodes['name'].NodeValue;
end;

procedure TXMLStampType.Set_Name(Value: Integer);
begin
  SetAttribute('name', Value);
end;

function TXMLStampType.Get_Icon: Integer;
begin
  Result := AttributeNodes['icon'].NodeValue;
end;

procedure TXMLStampType.Set_Icon(Value: Integer);
begin
  SetAttribute('icon', Value);
end;

function TXMLStampType.Get_Page: Integer;
begin
  Result := AttributeNodes['page'].NodeValue;
end;

procedure TXMLStampType.Set_Page(Value: Integer);
begin
  SetAttribute('page', Value);
end;

function TXMLStampType.Get_Rect: UnicodeString;
begin
  Result := AttributeNodes['rect'].Text;
end;

procedure TXMLStampType.Set_Rect(Value: UnicodeString);
begin
  SetAttribute('rect', Value);
end;

function TXMLStampType.Get_Subject: Integer;
begin
  Result := AttributeNodes['subject'].NodeValue;
end;

procedure TXMLStampType.Set_Subject(Value: Integer);
begin
  SetAttribute('subject', Value);
end;

function TXMLStampType.Get_Title: Integer;
begin
  Result := AttributeNodes['title'].NodeValue;
end;

procedure TXMLStampType.Set_Title(Value: Integer);
begin
  SetAttribute('title', Value);
end;

function TXMLStampType.Get_Appearance: Integer;
begin
  Result := ChildNodes['appearance'].NodeValue;
end;

procedure TXMLStampType.Set_Appearance(Value: Integer);
begin
  ChildNodes['appearance'].NodeValue := Value;
end;

function TXMLStampType.Get_Popup: IXMLPopupType;
begin
  Result := ChildNodes['popup'] as IXMLPopupType;
end;

{ TXMLStampTypeList }

function TXMLStampTypeList.Add: IXMLStampType;
begin
  Result := AddItem(-1) as IXMLStampType;
end;

function TXMLStampTypeList.Insert(const Index: Integer): IXMLStampType;
begin
  Result := AddItem(Index) as IXMLStampType;
end;

function TXMLStampTypeList.Get_Item(Index: Integer): IXMLStampType;
begin
  Result := List[Index] as IXMLStampType;
end;

{ TXMLPopupType }

function TXMLPopupType.Get_Flags: Integer;
begin
  Result := AttributeNodes['flags'].NodeValue;
end;

procedure TXMLPopupType.Set_Flags(Value: Integer);
begin
  SetAttribute('flags', Value);
end;

function TXMLPopupType.Get_Open: Integer;
begin
  Result := AttributeNodes['open'].NodeValue;
end;

procedure TXMLPopupType.Set_Open(Value: Integer);
begin
  SetAttribute('open', Value);
end;

function TXMLPopupType.Get_Page: Integer;
begin
  Result := AttributeNodes['page'].NodeValue;
end;

procedure TXMLPopupType.Set_Page(Value: Integer);
begin
  SetAttribute('page', Value);
end;

function TXMLPopupType.Get_Rect: UnicodeString;
begin
  Result := AttributeNodes['rect'].Text;
end;

procedure TXMLPopupType.Set_Rect(Value: UnicodeString);
begin
  SetAttribute('rect', Value);
end;

{ TXMLLineType }

procedure TXMLLineType.AfterConstruction;
begin
  RegisterChildNode('popup', TXMLPopupType);
  inherited;
end;

function TXMLLineType.Get_Color: Integer;
begin
  Result := AttributeNodes['color'].NodeValue;
end;

procedure TXMLLineType.Set_Color(Value: Integer);
begin
  SetAttribute('color', Value);
end;

function TXMLLineType.Get_Creationdate: Integer;
begin
  Result := AttributeNodes['creationdate'].NodeValue;
end;

procedure TXMLLineType.Set_Creationdate(Value: Integer);
begin
  SetAttribute('creationdate', Value);
end;

function TXMLLineType.Get_Flags: Integer;
begin
  Result := AttributeNodes['flags'].NodeValue;
end;

procedure TXMLLineType.Set_Flags(Value: Integer);
begin
  SetAttribute('flags', Value);
end;

function TXMLLineType.Get_Start: UnicodeString;
begin
  Result := AttributeNodes['start'].Text;
end;

procedure TXMLLineType.Set_Start(Value: UnicodeString);
begin
  SetAttribute('start', Value);
end;

function TXMLLineType.Get_End_: UnicodeString;
begin
  Result := AttributeNodes['end'].Text;
end;

procedure TXMLLineType.Set_End_(Value: UnicodeString);
begin
  SetAttribute('end', Value);
end;

function TXMLLineType.Get_Date: Integer;
begin
  Result := AttributeNodes['date'].NodeValue;
end;

procedure TXMLLineType.Set_Date(Value: Integer);
begin
  SetAttribute('date', Value);
end;

function TXMLLineType.Get_Name: Integer;
begin
  Result := AttributeNodes['name'].NodeValue;
end;

procedure TXMLLineType.Set_Name(Value: Integer);
begin
  SetAttribute('name', Value);
end;

function TXMLLineType.Get_Page: Integer;
begin
  Result := AttributeNodes['page'].NodeValue;
end;

procedure TXMLLineType.Set_Page(Value: Integer);
begin
  SetAttribute('page', Value);
end;

function TXMLLineType.Get_Rect: UnicodeString;
begin
  Result := AttributeNodes['rect'].Text;
end;

procedure TXMLLineType.Set_Rect(Value: UnicodeString);
begin
  SetAttribute('rect', Value);
end;

function TXMLLineType.Get_Subject: Integer;
begin
  Result := AttributeNodes['subject'].NodeValue;
end;

procedure TXMLLineType.Set_Subject(Value: Integer);
begin
  SetAttribute('subject', Value);
end;

function TXMLLineType.Get_Title: Integer;
begin
  Result := AttributeNodes['title'].NodeValue;
end;

procedure TXMLLineType.Set_Title(Value: Integer);
begin
  SetAttribute('title', Value);
end;

function TXMLLineType.Get_Width: UnicodeString;
begin
  Result := AttributeNodes['width'].Text;
end;

procedure TXMLLineType.Set_Width(Value: UnicodeString);
begin
  SetAttribute('width', Value);
end;

function TXMLLineType.Get_Style: Integer;
begin
  Result := AttributeNodes['style'].NodeValue;
end;

procedure TXMLLineType.Set_Style(Value: Integer);
begin
  SetAttribute('style', Value);
end;

function TXMLLineType.Get_Interiorcolor: Integer;
begin
  Result := AttributeNodes['interior-color'].NodeValue;
end;

procedure TXMLLineType.Set_Interiorcolor(Value: Integer);
begin
  SetAttribute('interior-color', Value);
end;

function TXMLLineType.Get_Popup: IXMLPopupType;
begin
  Result := ChildNodes['popup'] as IXMLPopupType;
end;

{ TXMLLineTypeList }

function TXMLLineTypeList.Add: IXMLLineType;
begin
  Result := AddItem(-1) as IXMLLineType;
end;

function TXMLLineTypeList.Insert(const Index: Integer): IXMLLineType;
begin
  Result := AddItem(Index) as IXMLLineType;
end;

function TXMLLineTypeList.Get_Item(Index: Integer): IXMLLineType;
begin
  Result := List[Index] as IXMLLineType;
end;

{ TXMLFType }

function TXMLFType.Get_Href: UnicodeString;
begin
  Result := AttributeNodes['href'].Text;
end;

procedure TXMLFType.Set_Href(Value: UnicodeString);
begin
  SetAttribute('href', Value);
end;

{ TXMLIdsType }

function TXMLIdsType.Get_Original: Integer;
begin
  Result := AttributeNodes['original'].NodeValue;
end;

procedure TXMLIdsType.Set_Original(Value: Integer);
begin
  SetAttribute('original', Value);
end;

function TXMLIdsType.Get_Modified: Integer;
begin
  Result := AttributeNodes['modified'].NodeValue;
end;

procedure TXMLIdsType.Set_Modified(Value: Integer);
begin
  SetAttribute('modified', Value);
end;

end.