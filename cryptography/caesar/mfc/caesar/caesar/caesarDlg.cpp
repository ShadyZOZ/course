
// caesarDlg.cpp : implementation file
//

#include "stdafx.h"
#include "caesar.h"
#include "caesarDlg.h"
#include "afxdialogex.h"

#ifdef _DEBUG
#define new DEBUG_NEW
#endif


// CAboutDlg dialog used for App About

class CAboutDlg : public CDialogEx
{
public:
	CAboutDlg();

// Dialog Data
	enum { IDD = IDD_ABOUTBOX };

	protected:
	virtual void DoDataExchange(CDataExchange* pDX);    // DDX/DDV support

// Implementation
protected:
	DECLARE_MESSAGE_MAP()
};

CAboutDlg::CAboutDlg() : CDialogEx(CAboutDlg::IDD)
{
}

void CAboutDlg::DoDataExchange(CDataExchange* pDX)
{
	CDialogEx::DoDataExchange(pDX);
}

BEGIN_MESSAGE_MAP(CAboutDlg, CDialogEx)
END_MESSAGE_MAP()


// CcaesarDlg dialog



CcaesarDlg::CcaesarDlg(CWnd* pParent /*=NULL*/)
	: CDialogEx(CcaesarDlg::IDD, pParent)
	, m_plaintext(_T(""))
	, m_crypt(_T(""))
	, m_decrypt(_T(""))
	, m_step(0)
{
	m_hIcon = AfxGetApp()->LoadIcon(IDR_MAINFRAME);
}

void CcaesarDlg::DoDataExchange(CDataExchange* pDX)
{
	CDialogEx::DoDataExchange(pDX);
	DDX_Text(pDX, IDC_EDITPLAINTEXT, m_plaintext);
	DDX_Text(pDX, IDC_EDITCRYPT, m_crypt);
	DDX_Text(pDX, IDC_EDITDECRYPT, m_decrypt);
	DDX_Text(pDX, IDC_EDITSTEP, m_step);
}

BEGIN_MESSAGE_MAP(CcaesarDlg, CDialogEx)
	ON_WM_SYSCOMMAND()
	ON_WM_PAINT()
	ON_WM_QUERYDRAGICON()
	ON_BN_CLICKED(IDC_BUTTON2, &CcaesarDlg::OnBnClickedButton2)
	ON_BN_CLICKED(IDC_BUTTON1, &CcaesarDlg::OnBnClickedButton1)
END_MESSAGE_MAP()


// CcaesarDlg message handlers

BOOL CcaesarDlg::OnInitDialog()
{
	CDialogEx::OnInitDialog();

	// Add "About..." menu item to system menu.

	// IDM_ABOUTBOX must be in the system command range.
	ASSERT((IDM_ABOUTBOX & 0xFFF0) == IDM_ABOUTBOX);
	ASSERT(IDM_ABOUTBOX < 0xF000);

	CMenu* pSysMenu = GetSystemMenu(FALSE);
	if (pSysMenu != NULL)
	{
		BOOL bNameValid;
		CString strAboutMenu;
		bNameValid = strAboutMenu.LoadString(IDS_ABOUTBOX);
		ASSERT(bNameValid);
		if (!strAboutMenu.IsEmpty())
		{
			pSysMenu->AppendMenu(MF_SEPARATOR);
			pSysMenu->AppendMenu(MF_STRING, IDM_ABOUTBOX, strAboutMenu);
		}
	}

	// Set the icon for this dialog.  The framework does this automatically
	//  when the application's main window is not a dialog
	SetIcon(m_hIcon, TRUE);			// Set big icon
	SetIcon(m_hIcon, FALSE);		// Set small icon

	// TODO: Add extra initialization here

	return TRUE;  // return TRUE  unless you set the focus to a control
}

void CcaesarDlg::OnSysCommand(UINT nID, LPARAM lParam)
{
	if ((nID & 0xFFF0) == IDM_ABOUTBOX)
	{
		CAboutDlg dlgAbout;
		dlgAbout.DoModal();
	}
	else
	{
		CDialogEx::OnSysCommand(nID, lParam);
	}
}

// If you add a minimize button to your dialog, you will need the code below
//  to draw the icon.  For MFC applications using the document/view model,
//  this is automatically done for you by the framework.

void CcaesarDlg::OnPaint()
{
	if (IsIconic())
	{
		CPaintDC dc(this); // device context for painting

		SendMessage(WM_ICONERASEBKGND, reinterpret_cast<WPARAM>(dc.GetSafeHdc()), 0);

		// Center icon in client rectangle
		int cxIcon = GetSystemMetrics(SM_CXICON);
		int cyIcon = GetSystemMetrics(SM_CYICON);
		CRect rect;
		GetClientRect(&rect);
		int x = (rect.Width() - cxIcon + 1) / 2;
		int y = (rect.Height() - cyIcon + 1) / 2;

		// Draw the icon
		dc.DrawIcon(x, y, m_hIcon);
	}
	else
	{
		CDialogEx::OnPaint();
	}
}

// The system calls this function to obtain the cursor to display while the user drags
//  the minimized window.
HCURSOR CcaesarDlg::OnQueryDragIcon()
{
	return static_cast<HCURSOR>(m_hIcon);
}


void CcaesarDlg::OnBnClickedButton1()
{
	UpdateData(TRUE);
	m_crypt = m_plaintext;
	for (int i = 0; i < m_plaintext.GetLength(); i++)
	{
		if (m_plaintext.GetAt(i) >= 97 && m_plaintext.GetAt(i) <= 122)
		{
			m_crypt.SetAt(i, 97 + ((m_plaintext.GetAt(i) + m_step) - 97) % 26);
		}
		if (m_plaintext.GetAt(i) >= 65 && m_plaintext.GetAt(i) <= 90)
		{
			m_crypt.SetAt(i, 65 + ((m_plaintext.GetAt(i) + m_step) - 65) % 26);
		}
		if (m_plaintext.GetAt(i) >= 48 && m_plaintext.GetAt(i) <= 57)
		{
			m_crypt.SetAt(i, 48 + ((m_plaintext.GetAt(i) + m_step) - 48) % 10);
		}
		if (m_plaintext.GetAt(i) >= 33 && m_plaintext.GetAt(i) <= 47)
		{
			m_crypt.SetAt(i, 33 + ((m_plaintext.GetAt(i) + m_step) - 33) % 15);
		}
		if (m_plaintext.GetAt(i) >= 58 && m_plaintext.GetAt(i) <= 64)
		{
			m_crypt.SetAt(i, 58 + ((m_plaintext.GetAt(i) + m_step) - 58) % 7);
		}
		if (m_plaintext.GetAt(i) >= 91 && m_plaintext.GetAt(i) <= 96)
		{
			m_crypt.SetAt(i, 91 + ((m_plaintext.GetAt(i) + m_step) - 91) % 6);
		}
		if (m_plaintext.GetAt(i) >= 123 && m_plaintext.GetAt(i) <= 126)
		{
			m_crypt.SetAt(i, 123 + ((m_plaintext.GetAt(i) + m_step) - 123) % 4);
		}
	}
		UpdateData(FALSE);
}



void CcaesarDlg::OnBnClickedButton2()
{
	UpdateData(TRUE);
	m_decrypt = m_crypt;
	for (int i = 0; i < m_crypt.GetLength(); i++)
	{
		if (m_crypt.GetAt(i) >= 97 && m_crypt.GetAt(i) <= 122)
		{
			m_decrypt.SetAt(i, 122 - (122 - (m_crypt.GetAt(i) - m_step)) % 26);
		}
		if (m_crypt.GetAt(i) >= 65 && m_crypt.GetAt(i) <= 90)
		{
			m_decrypt.SetAt(i, 90 - (90 - (m_crypt.GetAt(i) - m_step)) % 26);
		}
		if (m_crypt.GetAt(i) >= 48 && m_crypt.GetAt(i) <= 57)
		{
			m_decrypt.SetAt(i, 57 - (57 - (m_crypt.GetAt(i) - m_step)) % 10);
		}
		if (m_crypt.GetAt(i) >= 33 && m_crypt.GetAt(i) <= 47)
		{
			m_decrypt.SetAt(i, 47 - (47 - (m_crypt.GetAt(i) - m_step)) % 15);
		}
		if (m_crypt.GetAt(i) >= 58 && m_crypt.GetAt(i) <= 64)
		{
			m_decrypt.SetAt(i, 64 - (64 - (m_crypt.GetAt(i) - m_step)) % 7);
		}
		if (m_crypt.GetAt(i) >= 91 && m_crypt.GetAt(i) <= 96)
		{
			m_decrypt.SetAt(i, 96 - (96 - (m_crypt.GetAt(i) - m_step)) % 6);
		}
		if (m_crypt.GetAt(i) >= 123 && m_crypt.GetAt(i) <= 126)
		{
			m_decrypt.SetAt(i, 126 - (126 - (m_crypt.GetAt(i) - m_step)) % 4);
		}
	}
	UpdateData(FALSE);
}
