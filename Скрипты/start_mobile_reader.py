# -*- coding: utf-8 -*-
"""
Мобильный веб-ридер лекций и конспектов ИТМО
Запускает локальный веб-сервер, доступный с любого телефона/планшета в той же Wi-Fi сети.
"""

import http.server
import socketserver
import os
import socket
import urllib.parse
import json
import re

PORT = 8080
WORKSPACE_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))

def get_local_ip():
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        s.connect(("8.8.8.8", 80))
        ip = s.getsockname()[0]
        s.close()
        return ip
    except Exception:
        return "127.0.0.1"

class LectureViewerHandler(http.server.SimpleHTTPRequestHandler):
    def translate_path(self, path):
        path = urllib.parse.unquote(path)
        if path == "/" or path == "":
            return os.path.join(WORKSPACE_DIR, "index_web_reader.html")
        
        if path == "/api/notes":
            return path
            
        clean_rel = path.lstrip("/")
        full_path = os.path.join(WORKSPACE_DIR, clean_rel)
        return full_path

    def do_GET(self):
        req_path = urllib.parse.unquote(self.path)
        
        if req_path == "/api/notes":
            self.send_response(200)
            self.send_header("Content-Type", "application/json; charset=utf-8")
            self.send_header("Access-Control-Allow-Origin", "*")
            self.end_headers()
            
            notes = []
            notes_dir = os.path.join(WORKSPACE_DIR, "Конспекты")
            if os.path.exists(notes_dir):
                for f in sorted(os.listdir(notes_dir), reverse=True):
                    if f.endswith(".md"):
                        p = os.path.join(notes_dir, f)
                        title = f.replace(".md", "")
                        notes.append({
                            "title": title,
                            "filename": f,
                            "path": f"/Конспекты/{urllib.parse.quote(f)}",
                            "size": os.path.getsize(p)
                        })
            
            extra_docs = [
                {"title": "🏠 Главная", "path": f"/{urllib.parse.quote('🏠 Главная.md')}"},
                {"title": "📋 TODO (Задачи)", "path": "/TODO.md"},
                {"title": "🚀 Каталог возможностей ИТМО", "path": "/OPPORTUNITIES.md"}
            ]
            
            resp = {
                "notes": notes,
                "extra": extra_docs,
                "workspace": "ИТМО Software Engineering"
            }
            self.wfile.write(json.dumps(resp, ensure_ascii=False).encode("utf-8"))
            return

        if req_path == "/" or req_path == "":
            self.send_response(200)
            self.send_header("Content-Type", "text/html; charset=utf-8")
            self.end_headers()
            self.wfile.write(HTML_TEMPLATE.encode("utf-8"))
            return

        return super().do_GET()

HTML_TEMPLATE = """<!DOCTYPE html>
<html lang="ru">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>ИТМО Лекции & Конспекты | Mobile Reader</title>
  <script src="https://cdn.tailwindcss.com"></script>
  <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.0/css/all.min.css">
  <script src="https://cdn.jsdelivr.net/npm/marked/marked.min.js"></script>
  <script id="MathJax-script" async src="https://cdn.jsdelivr.net/npm/mathjax@3/es5/tex-mml-chtml.js"></script>
  <style>
    body {
      background-color: #0b1120;
      color: #e2e8f0;
      font-family: system-ui, -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif;
    }
    .markdown-body h1 { font-size: 1.5rem; font-weight: 700; margin-top: 1.5rem; margin-bottom: 0.75rem; color: #38bdf8; }
    .markdown-body h2 { font-size: 1.25rem; font-weight: 600; margin-top: 1.25rem; margin-bottom: 0.5rem; color: #f8fafc; border-bottom: 1px solid #334155; padding-bottom: 0.25rem; }
    .markdown-body h3 { font-size: 1.1rem; font-weight: 600; margin-top: 1rem; margin-bottom: 0.5rem; color: #bae6fd; }
    .markdown-body p { margin-bottom: 0.75rem; line-height: 1.6; }
    .markdown-body ul, .markdown-body ol { margin-left: 1.25rem; margin-bottom: 0.75rem; list-style-type: disc; }
    .markdown-body table { width: 100%; border-collapse: collapse; margin-bottom: 1rem; font-size: 0.85rem; }
    .markdown-body th, .markdown-body td { border: 1px solid #334155; padding: 0.5rem; text-align: left; }
    .markdown-body th { background: #1e293b; color: #38bdf8; font-weight: 600; }
    .markdown-body blockquote { border-left: 4px solid #38bdf8; padding-left: 1rem; margin-left: 0; margin-bottom: 1rem; color: #94a3b8; background: #1e293b50; padding-top: 0.5rem; padding-bottom: 0.5rem; border-radius: 0 0.5rem 0.5rem 0; }
    .markdown-body code { background: #1e293b; color: #38bdf8; padding: 0.2rem 0.4rem; border-radius: 0.25rem; font-size: 0.85em; font-family: monospace; }
    .custom-scroll::-webkit-scrollbar { width: 4px; height: 4px; }
    .custom-scroll::-webkit-scrollbar-thumb { background: #475569; border-radius: 4px; }
  </style>
</head>
<body class="min-h-screen flex flex-col md:flex-row custom-scroll">

  <!-- Mobile Top Bar -->
  <header class="md:hidden bg-slate-900 border-b border-slate-800 p-3.5 flex items-center justify-between sticky top-0 z-30">
    <div class="flex items-center gap-2">
      <i class="fa-solid fa-graduation-cap text-sky-400"></i>
      <span class="font-bold text-sm text-white">ИТМО Конспекты</span>
    </div>
    <button onclick="toggleSidebar()" class="p-2 bg-slate-800 rounded-lg text-slate-300">
      <i class="fa-solid fa-bars"></i>
    </button>
  </header>

  <!-- Sidebar / Notes List -->
  <aside id="sidebar" class="fixed md:static inset-y-0 left-0 z-40 w-72 bg-slate-900 border-r border-slate-800 p-4 transform -translate-x-full md:translate-x-0 transition-transform duration-200 flex flex-col justify-between shadow-2xl md:shadow-none">
    <div class="space-y-4">
      <div class="flex items-center justify-between">
        <div class="flex items-center gap-2">
          <div class="w-8 h-8 rounded-lg bg-sky-500/20 text-sky-400 flex items-center justify-center font-bold text-sm">
            <i class="fa-solid fa-book-open"></i>
          </div>
          <div>
            <h1 class="font-bold text-sm text-white">Лекции & Hub</h1>
            <p class="text-[10px] text-slate-400">ИТМО • 09.03.02 SE</p>
          </div>
        </div>
        <button onclick="toggleSidebar()" class="md:hidden text-slate-400 p-1">
          <i class="fa-solid fa-xmark"></i>
        </button>
      </div>

      <!-- Search -->
      <div class="relative">
        <i class="fa-solid fa-magnifying-glass absolute left-3 top-1/2 -translate-y-1/2 text-xs text-slate-400"></i>
        <input type="text" id="searchInput" placeholder="Поиск по конспектам..." 
               class="w-full bg-slate-800/80 border border-slate-700 text-xs text-slate-200 rounded-xl pl-8 pr-3 py-1.5 focus:outline-none focus:border-sky-500"
               oninput="filterNotes()">
      </div>

      <!-- Notes Navigation List -->
      <nav class="space-y-1 max-h-[60vh] overflow-y-auto custom-scroll pr-1">
        <span class="text-[10px] font-semibold text-slate-400 uppercase tracking-wider block px-2 mb-1">Разделы & Задачи</span>
        <div id="extraLinks" class="space-y-0.5"></div>

        <span class="text-[10px] font-semibold text-slate-400 uppercase tracking-wider block px-2 mt-3 mb-1">Конспекты лекций</span>
        <div id="notesList" class="space-y-0.5"></div>
      </nav>
    </div>

    <div class="pt-3 border-t border-slate-800 text-[10px] text-slate-400 flex items-center justify-between">
      <span><i class="fa-solid fa-wifi text-emerald-400 mr-1"></i> Локальная сеть</span>
      <button onclick="loadNotesList()" class="hover:text-white"><i class="fa-solid fa-rotate"></i></button>
    </div>
  </aside>

  <!-- Overlay for mobile sidebar -->
  <div id="sidebarOverlay" onclick="toggleSidebar()" class="fixed inset-0 bg-black/60 z-30 hidden md:hidden"></div>

  <!-- Main Content Area -->
  <main class="flex-1 min-w-0 p-4 sm:p-8 max-w-4xl mx-auto space-y-4">
    <!-- Header of current note -->
    <div class="bg-slate-900/80 border border-slate-800 rounded-2xl p-4 flex flex-col sm:flex-row sm:items-center justify-between gap-3 shadow-lg">
      <div class="min-w-0">
        <span id="noteCategory" class="text-[10px] font-semibold text-sky-400 uppercase tracking-wider">Конспект лекции</span>
        <h2 id="noteHeading" class="text-base sm:text-lg font-bold text-white truncate mt-0.5">Загрузка...</h2>
      </div>
      <div class="flex items-center gap-2">
        <button onclick="window.scrollTo({top: 0, behavior: 'smooth'})" class="p-2 bg-slate-800 hover:bg-slate-700 text-slate-300 rounded-xl text-xs">
          <i class="fa-solid fa-arrow-up"></i> Наверх
        </button>
      </div>
    </div>

    <!-- Rendered Markdown Content -->
    <article id="contentArea" class="markdown-body bg-slate-900/60 border border-slate-800/80 rounded-3xl p-5 sm:p-8 shadow-xl leading-relaxed text-sm">
      <div class="text-center py-12 text-slate-400">
        <i class="fa-solid fa-spinner fa-spin text-2xl text-sky-400 mb-2"></i>
        <p>Загрузка конспекта...</p>
      </div>
    </article>
  </main>

  <script>
    let allNotes = [];
    let extraDocs = [];
    let currentPath = '';

    async function loadNotesList() {
      try {
        const res = await fetch('/api/notes');
        const data = await res.json();
        allNotes = data.notes || [];
        extraDocs = data.extra || [];
        renderSidebar();

        if (!currentPath) {
          if (allNotes.length > 0) {
            loadNote(allNotes[0].path, allNotes[0].title);
          } else if (extraDocs.length > 0) {
            loadNote(extraDocs[0].path, extraDocs[0].title);
          }
        }
      } catch (err) {
        console.error('Error loading notes:', err);
      }
    }

    function renderSidebar() {
      const q = document.getElementById('searchInput').value.toLowerCase().trim();
      const notesContainer = document.getElementById('notesList');
      const extraContainer = document.getElementById('extraLinks');

      extraContainer.innerHTML = extraDocs.map(doc => `
        <button onclick="loadNote('${doc.path}', '${doc.title}')" 
                class="w-full text-left px-2.5 py-2 rounded-xl text-xs transition flex items-center gap-2 ${currentPath === doc.path ? 'bg-sky-500/20 text-sky-400 font-semibold border border-sky-500/30' : 'text-slate-300 hover:bg-slate-800'}">
          <i class="fa-regular fa-file-lines text-slate-400 text-xs"></i>
          <span class="truncate">${doc.title}</span>
        </button>
      `).join('');

      const filtered = allNotes.filter(n => !q || n.title.toLowerCase().includes(q));

      if (filtered.length === 0) {
        notesContainer.innerHTML = '<p class="text-[11px] text-slate-500 px-2 py-1">Ничего не найдено</p>';
        return;
      }

      notesContainer.innerHTML = filtered.map(note => `
        <button onclick="loadNote('${note.path}', '${note.title}')" 
                class="w-full text-left px-2.5 py-2 rounded-xl text-xs transition flex items-center gap-2 ${currentPath === note.path ? 'bg-sky-500/20 text-sky-400 font-semibold border border-sky-500/30' : 'text-slate-300 hover:bg-slate-800'}">
          <i class="fa-solid fa-graduation-cap text-xs ${currentPath === note.path ? 'text-sky-400' : 'text-slate-500'}"></i>
          <span class="truncate">${note.title}</span>
        </button>
      `).join('');
    }

    function filterNotes() {
      renderSidebar();
    }

    async function loadNote(path, title) {
      currentPath = path;
      renderSidebar();
      
      const overlay = document.getElementById('sidebarOverlay');
      const sidebar = document.getElementById('sidebar');
      sidebar.classList.add('-translate-x-full');
      overlay.classList.add('hidden');

      document.getElementById('noteHeading').innerText = title;
      const contentEl = document.getElementById('contentArea');
      contentEl.innerHTML = '<div class="text-center py-12 text-slate-400"><i class="fa-solid fa-spinner fa-spin text-2xl text-sky-400 mb-2"></i><p>Загрузка...</p></div>';

      try {
        const res = await fetch(path);
        let md = await res.text();
        
        if (md.startsWith('---')) {
          const parts = md.split('---');
          if (parts.length >= 3) {
            md = parts.slice(2).join('---').trim();
          }
        }

        let html = marked.parse(md);
        
        html = html.replace(/\\[\\[(.*?)\\|(.*?)\\]\\]/g, '<span class="text-sky-400 font-semibold underline cursor-pointer" onclick="handleWikilink(\\'$1\\')">$2</span>');
        html = html.replace(/\\[\\[(.*?)\\]\\]/g, '<span class="text-sky-400 font-semibold underline cursor-pointer" onclick="handleWikilink(\\'$1\\')">$1</span>');

        contentEl.innerHTML = html;

        if (window.MathJax && window.MathJax.typesetPromise) {
          MathJax.typesetPromise([contentEl]);
        }

        window.scrollTo({top: 0, behavior: 'smooth'});
      } catch (e) {
        contentEl.innerHTML = '<p class="text-rose-400">Ошибка загрузки файла</p>';
      }
    }

    function handleWikilink(link) {
      const found = allNotes.find(n => n.title.toLowerCase().includes(link.toLowerCase()) || n.filename.toLowerCase().includes(link.toLowerCase()));
      if (found) {
        loadNote(found.path, found.title);
      } else {
        const ex = extraDocs.find(d => d.title.toLowerCase().includes(link.toLowerCase()) || d.path.toLowerCase().includes(link.toLowerCase()));
        if (ex) loadNote(ex.path, ex.title);
      }
    }

    function toggleSidebar() {
      const sidebar = document.getElementById('sidebar');
      const overlay = document.getElementById('sidebarOverlay');
      sidebar.classList.toggle('-translate-x-full');
      overlay.classList.toggle('hidden');
    }

    loadNotesList();
  </script>
</body>
</html>
"""

def run():
    ip = get_local_ip()
    os.chdir(WORKSPACE_DIR)
    
    with socketserver.TCPServer(("", PORT), LectureViewerHandler) as httpd:
        print("=" * 60)
        print("🎓 ИТМО Mobile Lecture Server запущен!")
        print(f"📱 Для чтения лекций с телефона откройте в браузере:")
        print(f"👉 http://{ip}:{PORT}")
        print(f"💻 На этом компьютере: http://localhost:{PORT}")
        print("=" * 60)
        print("Нажмите Ctrl+C для остановки сервера.")
        try:
            httpd.serve_forever()
        except KeyboardInterrupt:
            print("\nСервер остановлен.")

if __name__ == "__main__":
    run()
